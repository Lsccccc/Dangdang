from pyleap import *
window.set_size(400,400)
bg=Rectangle(0,0,400,400,(0,0,64))
title=Text("当当0.2.0更新",20,330,40,"orange")
icon1=Sprite("https://rss.leaplearner.com/ud/production//69892/160066657267394.PNG",200,80,150,150)
texts=[
    Text("当当0.2.0更新内容：",30,280,20,"white"),
    Text("二级防，需要一个当当或两",30,250,20,"white"),
    Text("个防。",30,220,20,"white"),
    Text("图标见下图",30,190,20,"white"),
    Text("↓",30,160,20,"white"),
    Text("↓",30,130,20,"white"),
    Text("→ → →",30,100,20,"white"),
    ]
def draw(dt):
    bg.draw()
    title.draw()
    icon1.draw()
    for t in texts:
        t.draw()
repeat(draw)
run()
