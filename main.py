'''现存bug:
无
'''
#开始按钮的链接有两个：https://r.leaplearner.com/i/f3ec14.png和https://r.leaplearner.com/i/4dc731.png



#导入
from pyleap import *
import time
import random
import dangdang_audio.dangdang_audio as audio
from dangdang_sources import *

window.set_size(600,600)

#创建游戏中的图形、变量
start_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159359371639534.jpg",300,300,600,600)
start_button=Sprite("https://r.leaplearner.com/i/4dc731.png",300,250)
page="start"
AI_can_do_action=None
game_background=Sprite("https://r.leaplearner.com/i/6c4bc0.png",300,300,600,600)
win_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159444212323884.jpg",300,300,600,600)
lose_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159445800818334.jpg",300,230,800,800)
tip_window=None

#游戏指南
game_manual_button=Sprite("https://r.leaplearner.com/i/02efc0.png",550,550,50,50)
game_manual_pages=[
    Sprite("https://rss.leaplearner.com/ud/production//69892/159929235248654.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/159966446305432.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/159966447667244.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/160016136690931.jpg",300,300,400,400),
    ]
game_manual_quit_button=Sprite("https://r.leaplearner.com/i/dd02f1.png",470,470,50,50)
game_manual_page=0

#版本更新
update_button=Sprite("https://rss.leaplearner.com/ud/production//69892/160107697164759.jpg",150,550,200,50)
update_page=Sprite("https://rss.leaplearner.com/ud/production//69892/160107944840178.PNG",300,300,400,400)
update_quit_button=Sprite("https://r.leaplearner.com/i/dd02f1.png",470,470,50,50)


#完成出动作（技能）的主要变量
player_dangdangs=0
AI_dangdangs=0
player_protection_points=0
AI_protection_points=0
player_daggers=0
AI_daggers=0
player_level=0
AI_level=0

#动画相关
player_dynamic_icons=[Sprite("https://r.leaplearner.com/i/06ca74.png",300,250,100,100)]
AI_dynamic_icons=[Sprite("https://r.leaplearner.com/i/06ca74.png",300,350,100,100)]
playing_animation=False

#音频播放（有问题，暂时没有应用上）
will_play_audio=""
AI_will_play_audio=""
can_play_audio=False
AI_can_play_audio=False
play_win_or_lose_audio_times=0

#action_names为全局列表，便于用技能名字查找技能对象
action_names=[]
actions=[]

class Action:
    def __init__(self,name,TYPE,level,effects):
        '''
        Action类
        type 技能类型，如“攻击”“防御”
        level 技能等级，以0开始，判断输赢时有用
        name 技能中文名
        effects 技能效果：消耗与增加，列表
        probability AI选出各技能的概率
        pre_do() 玩家出此技能，并调用do()
        '''
        self.type=TYPE
        self.level=level
        self.name=name
        self.effects=effects
        self.probability=self.level+1
        action_names.append(self.name)
        actions.append(self)

    def pre_do(self):
        if icons[actions.index(self)].opacity<1:
            return None
        global player_dangdangs,player_protection_points,player_daggers,player_level
        do(self.name)
        #编译effects列表里的指令并执行
        for command in self.effects:
            if command=='special':
                pass
            else:
                _item=str(command[:4])
                _number=int(command[4:])
                if _item=='dang':
                    player_dangdangs+=_number
                elif _item=='dagr':
                    player_daggers+=_number
                elif _item=='prtp':
                    player_protection_points+=_number
                elif _item=='lvel':
                    player_level+=_number
                    
#创建对象     
dangdang=Action("当当","basic",0,["dang+1"])
dagger=Action("匕首","attack",0,["dang-1","dagr+1"])
defense1=Action("一级防","defense",0,["prtp+1"])
strike=Action("爆气","attack",1,["dang-2"])
exchange1=Action("逆转","exchange",0,["dang-1"])
defense2=Action("二级防","defense",1,["dang-1"])
double_dagger=Action("双刃","attack",1,["special"])
exchange2=Action("核逆","exchange",1,["dang-1"])
suicide=Action("自杀","suicide",0,["dang-0"])
ACTION=Action("ACTION","attack",2,["dang-3"])
quickly_upgrade=Action("快速升级","upgrade",0,["lvel+1"])

for i in actions:
    #这里控制AI选择的概率，相当于是一种策略
    i.probability+=int(i.type=="attack")*4#有攻击最好先出攻击
    i.probability+=int(not i.type=="suicide")*3#出“自sha”技能的概率很小，所以把不是自sha的技能的概率都增加3倍
    i.probability+=int(i.type=="defense")*2#出防御的概率也该稍微大一些

icons=[
    Sprite("https://rss.leaplearner.com/ud/production//69892/159912453130908.PNG",30,30,60,60),#当当dangdang
    Sprite("https://rss.leaplearner.com/ud/production//69892/159381880006242.PNG",30,95,60,60),#匕首dagger
    Sprite("https://rss.leaplearner.com/ud/production//69892/159919591565440.PNG",30,160,60,60),#一级防defense1
    Sprite("https://rss.leaplearner.com/ud/production//69892/159972887891696.PNG",95,95,60,60),#爆气strike
    Sprite("https://rss.leaplearner.com/ud/production//69892/160048231758593.PNG",30,225,60,60),#逆转exchange1
    Sprite("https://rss.leaplearner.com/ud/production//69892/160066657267394.PNG",95,160,60,60),#二级防defense2
    Sprite("https://rss.leaplearner.com/ud/production//69892/160225812821975.PNG",160,95,60,60),#双刃double_dagger
    Sprite("https://rss.leaplearner.com/ud/production//69892/160317201437317.PNG",95,225,60,60),#核逆exchange2
    Sprite("https://rss.leaplearner.com/ud/production//69892/160325829698599.PNG",30,290,60,60),#自sha suicide
    Sprite("https://rss.leaplearner.com/ud/production//69892/160344412782024.PNG",225,95,60,60),#ACTION
    Sprite("https://rss.leaplearner.com/ud/production//69892/160410676521047.PNG",30,355,60,60),#快速升级quickly_upgrade
    Sprite("https://rss.leaplearner.com/ud/production//69892/160410677685329.PNG",95,355,60,60),#终极升级powerful_upgrade
    Sprite("https://rss.leaplearner.com/ud/production//69892/160410678681287.PNG",30,420,60,60),#防+升级defense_upgrade_combine
    ]
for icon in icons:
    icon.opacity=0
AI_choices=["当当","当当","一级防","一级防","快速升级"]
do_things=[]
AI_do_things=[]
temp_do_thing=None
AI_temp_do_thing=None
can_judge=False

#输还是赢（True是赢，False是输，None是平）
win_or_lose=None
win_or_lose_reason=Text("",70,310,20,"black")
player_action_points_texts=[
    Text("",80,490,20,"black"),
    Text("",80,460,20,"black"),
    Text("",80,430,20,"black"),
    Text("",80,400,20,"black"),
    ]
the_action=None
the_AI_action=None

level_less=None
level_equal=None
level_more=None


def AI_do():
    global AI_action_doing,AI_temp_do_thing,AI_dangdangs,AI_protection_points,AI_daggers
    AI_temp_do_thing=random.choice(AI_choices)
    AI_do_things.append(AI_temp_do_thing)
    if AI_temp_do_thing=="当当":
        AI_dangdangs+=1
        
    elif AI_temp_do_thing=="匕首":
        AI_dangdangs-=1
        AI_daggers+=1
            
    elif AI_temp_do_thing=="一级防":
        AI_protection_points+=1

    elif AI_temp_do_thing=="爆气":
        AI_dangdangs-=2

    elif AI_temp_do_thing=="逆转":
        AI_dangdangs-=1

    elif AI_temp_do_thing=="二级防":
        AI_dangdangs-=1

    elif AI_temp_do_thing=="双刃":
        if AI_daggers>=2:
            AI_daggers-=2
        elif AI_daggers>=1 and AI_dangdangs>=1:
            AI_daggers-=1
            AI_dangdangs-=1
        elif AI_dangdangs>=2:
            AI_dangdangs-=2
    for a in range(len(actions)):
        if actions[a].name==AI_temp_do_thing:
            AI_dynamic_icons.append(Sprite(icons[a].src,300,550,100,100))

    
def do(action):
    global action_doing,temp_do_thing,AI_can_do_action,will_play_audio,can_play_audio
    temp_do_thing=action
    do_things.append(temp_do_thing)
    AI_can_do_action=True
    for a in range(len(actions)):
        if actions[a].name==action:
            player_dynamic_icons.append(Sprite(icons[a].src,300,50,100,100))
            
            


def Main(dt):
    window.clear()
    global in_start_interface,player_dangdangs,temp_do_thing,AI_temp_do_thing
    global can_judge,start_length,in_game_interface,in_final_interface,win_or_lose,AI_dangdangs
    global the_action,the_AI_action,AI_can_do_action,tip_window
    global game_manual_page,player_protection_points,AI_protection_points
    global level_less,level_equal,level_more,player_daggers,AI_daggers,will_play_audio,AI_will_play_audio
    global can_play_audio,AI_can_play_audio,playing_animation,mouse_on_icon
    #判断是在什么页面
    if page=="start":
        start_background.draw()
        start_button.draw()
    elif page=="game":
        game_background.draw()
        for i in icons:
            i.draw()
        for i in player_action_points_texts:
            i.draw()
        for i in player_dynamic_icons:
            i.draw()
        if player_dynamic_icons[-1].y<250:
            player_dynamic_icons[-1].y+=5
            playing_animation=True
            
        else:
            playing_animation=False
            if len(player_dynamic_icons)>2:
                player_dynamic_icons.pop(0)
            

        for i in AI_dynamic_icons:
            i.draw()
        if AI_dynamic_icons[-1].y>350:
            AI_dynamic_icons[-1].y-=5
        elif len(AI_dynamic_icons)>2:
            AI_dynamic_icons.pop(0)
                
        game_manual_button.draw()
        update_button.draw()
        if tip_window=="game_manual":
            for p in range(len(game_manual_pages)):
                if p==game_manual_page:
                    game_manual_pages[p].draw()
            game_manual_quit_button.draw()
        elif tip_window=="update":
            update_page.draw()
            update_quit_button.draw()
        player_action_points_texts[0].src="目前玩家的「当当」数：%d"%player_dangdangs
        player_action_points_texts[1].src="目前玩家的「防」数：%d"%player_protection_points
        player_action_points_texts[2].src="目前玩家的「匕首」数：%d"%player_daggers
        player_action_points_texts[3].src="目前玩家的级别：%d"%player_level
    elif page=="final":
        if win_or_lose==True:
            win_background.draw()
            
        elif win_or_lose==False:
            lose_background.draw()

    if len(AI_do_things)<1 and judge_have_action(suicide):
        try:
            AI_choices.remove("自杀")
        except:
            pass
        
    if AI_can_do_action:
        AI_do()
        AI_can_do_action=False

    if len(do_things)>=1 and len(AI_do_things)>=1 and len(do_things)==len(AI_do_things):
        can_judge=True
    else:
        can_judge=False
        
    if player_protection_points>=2:
        player_protection_points-=2
        player_dangdangs+=1
    if AI_protection_points>=2:
        AI_protection_points-=2
        AI_dangdangs+=1

    actions[0].player_can_do=True
    actions[1].player_can_do=player_dangdangs>=1
    actions[2].player_can_do=True
    actions[3].player_can_do=player_dangdangs>=2
    actions[4].player_can_do=player_dangdangs>=1
    actions[5].player_can_do=player_dangdangs>=1
    actions[6].player_can_do=player_dangdangs>=2 or (player_dangdangs>=1 and player_daggers>=1) or player_daggers>=2
    actions[7].player_can_do=player_dangdangs>=2
    actions[8].player_can_do=True
    actions[9].player_can_do=player_dangdangs>=3
    actions[10].player_can_do=True

    actions[0].AI_can_do=True
    actions[1].AI_can_do=AI_dangdangs>=1
    actions[2].AI_can_do=True
    actions[3].AI_can_do=AI_dangdangs>=2
    actions[4].AI_can_do=AI_dangdangs>=1
    actions[5].AI_can_do=AI_dangdangs>=1
    actions[6].AI_can_do=AI_dangdangs>=2 or (AI_dangdangs>=1 and AI_daggers>=1) or AI_daggers>=2
    actions[7].AI_can_do=AI_dangdangs>=2
    actions[8].AI_can_do=True
    actions[9].AI_can_do=AI_dangdangs>=3
    actions[10].AI_can_do=True
    
    for i in range(len(actions)):
        if actions[i].player_can_do==True:
            icons[i].opacity=1
        elif actions[i].player_can_do==False:
            icons[i].opacity=0
        if playing_animation==True:
            icons[i].opacity=0

    if can_judge:
        judge_win_or_lose(temp_do_thing,AI_temp_do_thing)
    for i in actions:
        #print(i.name,i.AI_can_do)
        if i.AI_can_do and (judge_have_action(i.name)==False):
            for j in range(i.probability):
                if not(i.type=="suicide" and len(AI_do_things)<1):
                    AI_choices.append(i.name)
                    
        if not i.AI_can_do:
            try:
                for j in range(i.probability):
                    AI_choices.remove(i.name)
            except ValueError:
                pass

    if (player_dangdangs or player_protection_points or AI_dangdangs or AI_protection_points)<0:
        if player_dangdangs<0:
            raise ValueError("这里程序出了bug：当当小于0了。可以微信上向我提出，谢谢！")
        elif player_protection_points<0:
            raise ValueError("这里程序出了bug：防小于0了。可以微信上向我提出，谢谢！")
        elif AI_dangdangs<0:
            raise ValueError("这里程序出了bug：小当的当当小于0了。可以微信上向我提出，谢谢！")
        elif AI_protection_points<0:
            raise ValueError("这里程序出了bug：小当的防小于0了。可以微信上向我提出，谢谢！")
        stop(Main)

    
def judge_have_action(AI_act):
    if AI_act in AI_choices:
         return True
    else:
         return False
        
def start():
    global page
    page="game"

def judge_win_or_lose(ACTION,AI_ACTION):
    global page,win_or_lose,the_action,the_AI_action
    global temp_do_thing,AI_temp_do_thing
    global level_less,level_equal,level_more
    the_action=actions[action_names.index(ACTION)]
    the_AI_action=actions[action_names.index(AI_ACTION)]

    judge_string=judge_rule[(the_action.type,the_AI_action.type)]
        
    if judge_string[0]=="F":
        level_less=False
    elif judge_string[0]=="N":
        level_less=None
    elif judge_string[0]=="T":
        level_less=True

    if judge_string[1]=="F":
        level_equal=False
    elif judge_string[1]=="N":
        level_equal=None
    elif judge_string[1]=="T":
        level_equal=True

    if judge_string[2]=="F":
        level_more=False
    elif judge_string[2]=="N":
        level_more=None
    elif judge_string[2]=="T":
        level_more=True
    
    if the_action.level<the_AI_action.level:
        win_or_lose=level_less
    elif the_action.level==the_AI_action.level:
        win_or_lose=level_equal
    elif the_action.level>the_AI_action.level:
        win_or_lose=level_more
    
    if win_or_lose==True:
        page="final"
        win_or_lose_reason.src="您用「%s」赢了小当的「%s」"%(temp_do_thing,AI_temp_do_thing)
    elif win_or_lose==False:
        page="final"
        win_or_lose_reason.src="小当用「%s」赢了你的「%s」"%(AI_temp_do_thing,temp_do_thing)
    if win_or_lose!=None:
        win_or_lose_reason.draw()
    
def game_manual():
    global tip_window
    tip_window="game_manual"
    

def quit_game_manual():
    global tip_window
    tip_window=None

def turn_game_manual_page_left():
    global game_manual_page,tip_window
    if tip_window!="game_manual":
        return None
    game_manual_page-=1
    if game_manual_page<0:
        game_manual_page=0

def turn_game_manual_page_right():
    global game_manual_page,tip_window
    if tip_window!="game_manual":
        return None
    game_manual_page+=1
    if game_manual_page>len(game_manual_pages)-1:
        game_manual_page=len(game_manual_pages)-1
            
def update():
    global tip_window
    tip_window="update"

def quit_update():
    global tip_window
    tip_window=None
    
def control_win_or_lose(dt):
    global play_win_or_lose_audio_times,page
    global player_dangdangs,temp_do_thing,AI_temp_do_thing
    global can_judge,start_length,in_game_interface,in_final_interface,win_or_lose,AI_dangdangs
    global the_action,the_AI_action,AI_can_do_action,tip_window
    global game_manual_page,player_protection_points,AI_protection_points
    global level_less,level_equal,level_more,player_daggers,AI_daggers,will_play_audio,AI_will_play_audio
    global can_play_audio,AI_can_play_audio,playing_animation,do_things,AI_do_things
    global player_dynamic_icons,AI_dynamic_icons,AI_choices,action_names
    
    if win_or_lose==True:
        audio.play("C:/Users/HP/Desktop/当当/当当の素材制作/当当の音频/成功音乐.WAV")
    elif win_or_lose==False:
        audio.play("C:/Users/HP/Desktop/当当/当当の素材制作/当当の音频/失败音乐.WAV")

    if win_or_lose!=None:
        page="game"
        AI_can_do_action=False
        tip_window=None
        #游戏指南
        game_manual_page=0
        #完成出动作的主要变量

        player_dangdangs=0
        AI_dangdangs=0
        player_protection_points=0
        AI_protection_points=0
        player_daggers=0
        AI_daggers=0

        #动画相关
        player_dynamic_icons=[Sprite("https://r.leaplearner.com/i/06ca74.png",300,250,100,100)]
        AI_dynamic_icons=[Sprite("https://r.leaplearner.com/i/06ca74.png",300,350,100,100)]
        playing_animation=False

        #音频播放
        will_play_audio=""
        AI_will_play_audio=""
        can_play_audio=False
        AI_can_play_audio=False
        play_win_or_lose_audio_times=0


        AI_choices=["当当","当当","一级防","一级防"]
        do_things=[]
        AI_do_things=[]
        temp_do_thing=None
        AI_temp_do_thing=None
        can_judge=False
        #输还是赢（True是赢，False是输，None是平）
        win_or_lose=None
        player_action_points_texts=[
            Text("",50,490,20,"black"),
            Text("",50,460,20,"black"),
            Text("",50,430,20,"black"),
            Text("",50,400,10,"black")
            ]
        the_action=None
        the_AI_action=None

'''
def control_audio(dt):
    global can_play_audio,will_play_audio
    if can_play_audio==True:
        can_play_audio=False
        audio.play(will_play_audio)

def AI_control_audio(dt):
    global AI_can_play_audio,AI_will_play_audio
    if AI_can_play_audio==True:
        AI_can_play_audio=False
        audio.play(AI_will_play_audio)
'''
def debug():
    pass

repeat(Main)
repeat(control_win_or_lose,1)
#repeat(control_audio)
#repeat(AI_control_audio)
start_button.on_press(start)

for i in range(len(actions)):
    icons[i].on_press(actions[i].pre_do)

key.D.on_press(debug)
game_manual_button.on_press(game_manual)
game_manual_quit_button.on_press(quit_game_manual)
key.left.on_press(turn_game_manual_page_left)
key.right.on_press(turn_game_manual_page_right)
update_button.on_press(update)
update_quit_button.on_press(quit_update)
run()
