from pyleap import *
window.set_size(400,400)
bg=Rectangle(0,0,400,400,(0,0,64))
title=Text("规则介绍",80,330,40,"white")
icon1=Sprite("https://rss.leaplearner.com/ud/production//69892/159919591565440.PNG",80,230,150,150)
icon2=Sprite("https://rss.leaplearner.com/ud/production//69892/159972887891696.PNG",80,80,150,150)
texts=[
    Text("        这是“一级防”图标。一",158,280,14,"white"),
    Text("级防，最低等级的防御型动",158,260,14,"white"),
    Text("作。不需要消耗“当当”部件，",158,240,14,"white"),
    Text("出完了以后会增加一个在防",158,220,14,"white"),
    Text("御类动作里专属的部件——",158,200,14,"white"),
    Text("就叫“防”。注意，两个“防”部",158,180,14,"white"),
    Text("件可以抵一个“当当”部件。",158,160,14,"white"),
    
    Text("        这是“爆气”图标。爆气",158,130,14,"white"),
    Text("是比匕首更高级的攻击型动",158,110,14,"white"),
    Text("作，一级防是防不住的。需",158,90,14,"white"),
    Text("要两个“当当”。（注：也可",158,70,14,"white"),
    Text("为1个当当+2个防，或者4",158,50,14,"white"),
    Text("个防。",158,30,14,"white"),
    Text("                                           ",158,10,14,"white")
    ]
def draw(dt):
    bg.draw()
    title.draw()
    icon1.draw()
    icon2.draw()
    for t in texts:
        t.draw()
repeat(draw)
run()
