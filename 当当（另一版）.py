#判断输赢主要思维：把各个动作划分等级和类型，存入属性，等级越低列表索引号就会越小
#开始按钮的链接有两个：https://r.leaplearner.com/i/f3ec14.png和https://r.leaplearner.com/i/4dc731.png
from pyleap import *
window.set_size(600,600)
import time
import random
start_interface_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159359371639534.jpg",300,300,600,600)
start_button=Sprite("https://r.leaplearner.com/i/4dc731.png",300,250)
page="start"
AI_can_do_action=None
game_background=Sprite("https://r.leaplearner.com/i/6c4bc0.png",300,300,600,600)
win_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159444212323884.jpg",300,300,600,600)
lose_background=Sprite("https://rss.leaplearner.com/ud/production//69892/159445800818334.jpg",300,230,800,800)
#游戏指南
in_game_manual=False
game_manual_button=Sprite("https://r.leaplearner.com/i/02efc0.png",550,550,50,50)
game_manual_pages=[
    Sprite("https://rss.leaplearner.com/ud/production//69892/159929235248654.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/159966446305432.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/159966447667244.jpg",300,300,400,400),
    Sprite("https://rss.leaplearner.com/ud/production//69892/160016136690931.jpg",300,300,400,400),
    ]
game_manual_quit_button=Sprite("https://r.leaplearner.com/i/dd02f1.png",470,470,50,50)
game_manual_page=0

win_or_lose_reason=Text("",130,310,20,"black")
#完成出动作的主要变量

dangdangs=0
AI_dangdangs=0
protection_points=0
AI_protection_points=0

action_effect=Text("",150,250,40,"red")
AI_action_effect=Text("",150,310,40,"blue")
icons=[
    Sprite("https://rss.leaplearner.com/ud/production//69892/159912453130908.PNG",30,30,60,60),#当当
    Sprite("https://rss.leaplearner.com/ud/production//69892/159381880006242.PNG",30,90,60,60),#匕首
    Sprite("https://rss.leaplearner.com/ud/production//69892/159919591565440.PNG",30,150,60,60),#一级防
    Sprite("https://rss.leaplearner.com/ud/production//69892/159972887891696.PNG",90,90,60,60),#爆气
    Sprite("https://rss.leaplearner.com/ud/production//69892/160048231758593.PNG",30,210,60,60),#逆转
    Sprite("https://rss.leaplearner.com/ud/production//69892/160066657267394.PNG",90,150,60,60),#二级防
    ]

AI_choices=["当当","一级防"]
have_action=False
do_things=[]
AI_do_things=[]
temp_do_thing=None
AI_temp_do_thing=None
testing_AI_action=None
'''判断输赢'''
action_names=[]
basic_action=["当当"]#基本型（只有一个）
attack_actions=["匕首","爆气"]#攻击型
defense_actions=["一级防"]#防御型
exchange_actions=["逆转"]#转换型
upgrade_actions=[]#升级型
defense_upgrade_action=[]#防升型（只有一个）
#这是临时变量，是动作名字在action_names里的索引号
action_number=None
AI_action_number=None
can_judge=False
#输还是赢（True是赢，False是输，None是平）
win_or_lose=None
value_txt=Text('AI_dangdangs:'+str(AI_dangdangs),60,150,12,"orange")
the_action=None
the_AI_action=None

def AI_do():
    global AI_action_doing,AI_temp_do_thing,AI_dangdangs,AI_protection_points
    AI_temp_do_thing=random.choice(AI_choices)
    AI_action_effect.src="小当："+str(AI_temp_do_thing)
    AI_do_things.append(AI_temp_do_thing)
    if AI_temp_do_thing=="当当":
        AI_dangdangs+=1
        
    if AI_temp_do_thing=="匕首":
        if AI_dangdangs>=1:
            AI_dangdangs-=1
            
    if AI_temp_do_thing=="一级防":
        AI_protection_points+=1

    if AI_temp_do_thing=="爆气":
        if AI_dangdangs>=2:
            AI_dangdangs-=2
def do(action):
    global action_doing,temp_do_thing,AI_can_do_action
    temp_do_thing=action
    action_effect.src="玩家："+temp_do_thing
    do_things.append(temp_do_thing)
    AI_can_do_action=True

class An_action:
    def __init__(self,name,TYPE,level):
        self.type=TYPE
        self.level=level
        self.name=name
        self.AI_is_have=None
        action_names.append(self.name)
 ########       
dangdang=An_action  (name="当当",      TYPE="basic_action",            level=0)
dagger=An_action       (name="匕首",      TYPE="attack_actions",        level=0)
defense1=An_action    (name="一级防",  TYPE="defense_actions",       level=0)
strike=An_action          (name="爆气",      TYPE="attack_actions",        level=1)
exchange=An_action   (name="逆转",      TYPE="exchange_actions",    level=0)
defense2=An_action    (name="二级防",   TYPE="defense_actions",      level=1)
########
actions=[dangdang,dagger,defense1,strike,exchange,defense2]
def Main(dt):
    window.clear()
    global in_start_interface,dangdangs,temp_do_thing,AI_temp_do_thing
    global can_judge,start_length,in_game_interface,in_final_interface,win_or_lose,AI_dangdangs
    global have_action,the_action,the_AI_action,AI_can_do_action,in_game_manual
    global game_manual_page,protection_points,AI_protection_points
    #判断是在什么页面
    if page=="start":
        start_interface_background.draw()
        start_button.draw()
    elif page=="game":
        game_background.draw()
        for i in icons:
            i.draw()
        action_effect.draw()
        AI_action_effect.draw()
        value_txt.draw()
        game_manual_button.draw()
        if in_game_manual==True:
            for p in range(len(game_manual_pages)):
                if p==game_manual_page:
                    game_manual_pages[p].draw()
            game_manual_quit_button.draw()
        try:
            value_txt.src="AI_choices:"+str(AI_choices)
        except AttributeError:
            pass
        else:
            pass
    elif page=="final":
        if win_or_lose==True:
            win_background.draw()
        elif win_or_lose==False:
            lose_background.draw()
        else:
            pass
        
    if AI_can_do_action:
        start_length=len(AI_do_things)
        AI_temp_do_thing=None
    if AI_can_do_action:
        AI_do()
        AI_can_do_action=False
    if len(do_things)>=1 and len(AI_do_things)>=1 and len(do_things)==len(AI_do_things):
        can_judge=True

    #游戏特殊机制：2个防会自动兑换成1个当当
    if protection_points>=2:
        protection_points-=2
        dangdangs+=1
    if AI_protection_points>=2:
        AI_protection_points-=2
        AI_dangdangs+=1
        
    #出匕首的条件
    if dangdangs>=1:
        icons[1].opacity=1
    else:
        icons[1].opacity=0.5

    #出爆气的条件
    if dangdangs>=2:
        icons[3].opacity=1
    else:
        icons[3].opacity=0.5

    #出逆转的条件
    if dangdangs>=1:
        icons[4].opacity=1
    else:
        icons[4].opacity=0.5
        
    if can_judge:
        judge_win_or_lose(temp_do_thing,AI_temp_do_thing)

    #出二级防的条件
    if dangdangs>=1:
        icons[5].opacity=1
    else:
        icons[5].opacity=0.5
    
    #AI（小当）出匕首的条件
    judge_have_action("匕首")
    if AI_dangdangs>=1 and dagger.AI_is_have==False:
        AI_choices.append("匕首")

    if AI_dangdangs<1:
        try:
            AI_choices.remove("匕首")
        except ValueError:
            pass
        
    #AI（小当）出爆气的条件
    judge_have_action("爆气")
    if AI_dangdangs>=2 and strike.AI_is_have==False:
        AI_choices.append("爆气")

    if AI_dangdangs<2:
        try:
            AI_choices.remove("爆气")
        except ValueError:
            pass

    #AI（小当）出逆转的条件
    judge_have_action("逆转")
    if AI_dangdangs>=1 and exchange.AI_is_have==False:
        AI_choices.append("逆转")

    if AI_dangdangs<1:
        try:
            AI_choices.remove("逆转")
        except ValueError:
            pass

    #AI（小当）出二级防的条件
    judge_have_action("二级防")
    if AI_dangdangs>=1 and dagger.AI_is_have==False:
        AI_choices.append("二级防")

    if AI_dangdangs<1:
        try:
            AI_choices.remove("二级防")
        except ValueError:
            pass
def judge_have_action(AI_act):
    global have_action,testing_AI_action
    for i in range(len(action_names)):
        if action_names[i]==AI_act:
            testing_AI_action=actions[i]
    try:
        AI_choices.index(AI_act)
    except ValueError:
        testing_AI_action.AI_is_have=False
    else:
        testing_AI_action.AI_is_have=True
def start():
    global page
    page="game"

def judge_win_or_lose(ACTION,AI_ACTION):
    global action_number,AI_action_number,page,win_or_lose,the_action,the_AI_action
    global temp_do_thing,AI_temp_do_thing
    for i in range(len(action_names)):
        if action_names[i]==ACTION:
            action_number=i
            the_action=actions[i]
    for i in range(len(action_names)):
        if action_names[i]==AI_ACTION:
            AI_action_number=i
            the_AI_action=actions[i]
    #玩家 VS 系统

    #基本 VS 基本
    if the_action.type=="basic_action" and the_AI_action.type=="basic_action":
        win_or_lose=None
    #基本 VS 攻击
    if the_action.type=="basic_action" and the_AI_action.type=="attack_actions":
        win_or_lose=False
    #基本 VS 防御
    if the_action.type=="basic_action" and the_AI_action.type=="defense_actions":
        win_or_lose=None
    #基本 VS 转换
    if the_action.type=="basic_action" and the_AI_action.type=="exchange_actions":
        win_or_lose=None
    #基本 VS 自杀
    #基本 VS 升级
    #攻击 VS 基本
    if the_action.type=="attack_actions" and the_AI_action.type=="basic_action":
        win_or_lose=True
    #攻击 VS 攻击
    if the_action.type=="attack_actions" and the_AI_action.type=="attack_actions":
        if the_action.level>the_AI_action.level:
            win_or_lose=True
        elif the_action.level<the_AI_action.level:
            win_or_lose=False
        elif the_action.level==the_AI_action.level:
            win_or_lose=None
    #攻击 VS 防御
    if the_action.type=="attack_actions" and the_AI_action.type=="defense_actions":
        if the_action.level>the_AI_action.level:
            win_or_lose=True
        elif the_action.level<the_AI_action.level:
            win_or_lose=None
        elif the_action.level==the_AI_action.level:
            win_or_lose=None
    #攻击 VS 转换
    if the_action.type=="attack_actions" and the_AI_action.type=="exchange_actions":
        if the_action.level>the_AI_action.level:
            win_or_lose=True
        elif the_action.level<the_AI_action.level:
            win_or_lose=False
        elif the_action.level==the_AI_action.level:
            win_or_lose=False
    #攻击 VS 自杀
    #攻击 VS 升级
    #防御 VS 基本
    if the_action.type=="defense_actions" and the_AI_action.type=="basic_action":
        win_or_lose=None
    #防御 VS 攻击
    if the_action.type=="defense_actions" and the_AI_action.type=="attack_actions":
        if the_action.level>the_AI_action.level:
            win_or_lose=None
        elif the_action.level<the_AI_action.level:
            win_or_lose=False
        elif the_action.level==the_AI_action.level:
            win_or_lose=None
    #防御 VS 防御
    if the_action.type=="defense_actions" and the_AI_action.type=="defense_actions":
        win_or_lose=None
    #防御 VS 转换
    if the_action.type=="defense_actions" and the_AI_action.type=="exchange_actions":
        win_or_lose=None
    #防御 VS 自杀
    #防御 VS 升级
    #转换 VS 基本
    if the_action.type=="exchange_actions" and the_AI_action.type=="basic_action":
        win_or_lose=None
    #转换 VS 攻击
    if the_action.type=="exchange_actions" and the_AI_action.type=="attack_actions":
        if the_action.level>the_AI_action.level:
            win_or_lose=True
        elif the_action.level<the_AI_action.level:
            win_or_lose=False
        elif the_action.level==the_AI_action.level:
            win_or_lose=True
    #转换 VS 防御
    if the_action.type=="exchange_actions" and the_AI_action.type=="defense_actions":
        win_or_lose=None
    #转换 VS 转换
    if the_action.type=="exchange_actions" and the_AI_action.type=="exchange_actions":
        win_or_lose=None
    #转换 VS 自杀
    #转换 VS 升级
    #自杀 VS 基本
    #自杀 VS 攻击
    #自杀 VS 防御
    #自杀 VS 转换
    #自杀 VS 自杀
    #自杀 VS 升级
    #升级 VS 基本
    #升级 VS 攻击
    #升级 VS 防御
    #升级 VS 转换
    #升级 VS 自杀
    #升级 VS 升级
    if win_or_lose==True:
        page="final"
        win_or_lose_reason.src="您用%s赢了小当的%s"%(temp_do_thing,AI_temp_do_thing)
    elif win_or_lose==False:
        page="final"
        win_or_lose_reason.src="小当用%s赢了你的%s"%(AI_temp_do_thing,temp_do_thing)
    win_or_lose_reason.draw()

    
def do_dangdang():
    #你出了当当，当当就+1
    global dangdangs
    do("当当")
    dangdangs+=1
        
def do_dagger():
    #事件是重复侦测，所以要先过一道关
    if icons[1].opacity<1:
        return None
    #出匕首会消耗一个当当
    global dangdangs
    do("匕首")
    dangdangs-=1
    
def do_defense1():
    global protection_points
    do("一级防")
    protection_points+=1

def do_strike():
    if icons[3].opacity<1:
        return None
    #出爆气会消耗两个当当
    global dangdangs
    do("爆气")
    dangdangs-=2

def do_exchange():
    if icons[4].opacity<1:
        return None
    #出逆转会消耗一个当当
    global dangdangs
    do("逆转")
    dangdangs-=1

def do_defense2():
    if icons[5].opacity<1:
        return None
    global dangdangs
    do("二级防")
    dangdangs-=1
    
def game_manual():
    global in_game_manual
    in_game_manual=True

def quit_game_manual():
    global in_game_manual
    in_game_manual=False

def turn_game_manual_page_left():
    global game_manual_page,in_game_manual
    if in_game_manual==False:
        return None
    game_manual_page-=1
    if game_manual_page<0:
        game_manual_page=0

def turn_game_manual_page_right():
    global game_manual_page,in_game_manual
    if in_game_manual==False:
        return None
    game_manual_page+=1
    if game_manual_page>len(game_manual_pages)-1:
        game_manual_page=len(game_manual_pages)-1
            
    
        
repeat(Main)
start_button.on_press(start)
icons[0].on_press(do_dangdang)
icons[1].on_press(do_dagger)
icons[2].on_press(do_defense1)
icons[3].on_press(do_strike)
icons[4].on_press(do_exchange)
icons[5].on_press(do_defense2)
game_manual_button.on_press(game_manual)
game_manual_quit_button.on_press(quit_game_manual)
key.left.on_press(turn_game_manual_page_left)
key.right.on_press(turn_game_manual_page_right)
run()
