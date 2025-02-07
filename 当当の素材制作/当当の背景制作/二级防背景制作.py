from pyleap import *
window.set_size(500,500)
bg=Rectangle(0,0,500,500,"white")
blocks=[
    #1
    Rectangle(0,450,50,50,"yellow"),
    Rectangle(50,450,50,50,"yellow"),
    Rectangle(100,450,50,50,"yellow"),
    Rectangle(150,450,50,50,"yellow"),
    Rectangle(200,450,50,50,"yellow"),
    Rectangle(250,450,50,50,"yellow"),
    Rectangle(300,450,50,50,"yellow"),
    Rectangle(350,450,50,50,"yellow"),
    Rectangle(400,450,50,50,"yellow"),
    Rectangle(450,450,50,50,"yellow"),
    #2
    Rectangle(0,400,50,50,"yellow"),
    Rectangle(50,400,50,50,"yellow"),
    Rectangle(100,400,50,50,"yellow"),
    Rectangle(150,400,50,50,"red"),
    Rectangle(200,400,50,50,"red"),
    Rectangle(250,400,50,50,"red"),
    Rectangle(300,400,50,50,"red"),
    Rectangle(350,400,50,50,"yellow"),
    Rectangle(400,400,50,50,"yellow"),
    Rectangle(450,400,50,50,"yellow"),
    #3
    Rectangle(0,350,50,50,"yellow"),
    Rectangle(50,350,50,50,"yellow"),
    Rectangle(100,350,50,50,"red"),
    Rectangle(150,350,50,50,"brown"),
    Rectangle(200,350,50,50,"brown"),
    Rectangle(250,350,50,50,"brown"),
    Rectangle(300,350,50,50,"brown"),
    Rectangle(350,350,50,50,"red"),
    Rectangle(400,350,50,50,"yellow"),
    Rectangle(450,350,50,50,"yellow"),
    #4
    Rectangle(0,300,50,50,"yellow"),
    Rectangle(50,300,50,50,"yellow"),
    Rectangle(100,300,50,50,"red"),
    Rectangle(150,300,50,50,"brown"),
    Rectangle(200,300,50,50,"brown"),
    Rectangle(250,300,50,50,"brown"),
    Rectangle(300,300,50,50,"brown"),
    Rectangle(350,300,50,50,"red"),
    Rectangle(400,300,50,50,"yellow"),
    Rectangle(450,300,50,50,"yellow"),
    #5
    Rectangle(0,250,50,50,"yellow"),
    Rectangle(50,250,50,50,"yellow"),
    Rectangle(100,250,50,50,"red"),
    Rectangle(150,250,50,50,"brown"),
    Rectangle(200,250,50,50,"brown"),
    Rectangle(250,250,50,50,"brown"),
    Rectangle(300,250,50,50,"brown"),
    Rectangle(350,250,50,50,"red"),
    Rectangle(400,250,50,50,"yellow"),
    Rectangle(450,250,50,50,"yellow"),
    #6
    Rectangle(0,200,50,50,"yellow"),
    Rectangle(50,200,50,50,"yellow"),
    Rectangle(100,200,50,50,"red"),
    Rectangle(150,200,50,50,"brown"),
    Rectangle(200,200,50,50,"brown"),
    Rectangle(250,200,50,50,"brown"),
    Rectangle(300,200,50,50,"brown"),
    Rectangle(350,200,50,50,"red"),
    Rectangle(400,200,50,50,"yellow"),
    Rectangle(450,200,50,50,"yellow"),
    #7
    Rectangle(0,150,50,50,"yellow"),
    Rectangle(50,150,50,50,"yellow"),
    Rectangle(100,150,50,50,"red"),
    Rectangle(150,150,50,50,"brown"),
    Rectangle(200,150,50,50,"brown"),
    Rectangle(250,150,50,50,"brown"),
    Rectangle(300,150,50,50,"brown"),
    Rectangle(350,150,50,50,"red"),
    Rectangle(400,150,50,50,"yellow"),
    Rectangle(450,150,50,50,"yellow"),
    #8
    Rectangle(0,100,50,50,"yellow"),
    Rectangle(50,100,50,50,"yellow"),
    Rectangle(100,100,50,50,"yellow"),
    Rectangle(150,100,50,50,"red"),
    Rectangle(200,100,50,50,"brown"),
    Rectangle(250,100,50,50,"brown"),
    Rectangle(300,100,50,50,"red"),
    Rectangle(350,100,50,50,"yellow"),
    Rectangle(400,100,50,50,"yellow"),
    Rectangle(450,100,50,50,"yellow"),
    #9
    Rectangle(0,50,50,50,"yellow"),
    Rectangle(50,50,50,50,"yellow"),
    Rectangle(100,50,50,50,"yellow"),
    Rectangle(150,50,50,50,"yellow"),
    Rectangle(200,50,50,50,"red"),
    Rectangle(250,50,50,50,"red"),
    Rectangle(300,50,50,50,"yellow"),
    Rectangle(350,50,50,50,"yellow"),
    Rectangle(400,50,50,50,"yellow"),
    Rectangle(450,50,50,50,"yellow"),
    #10
    Rectangle(0,0,50,50,"yellow"),
    Rectangle(50,0,50,50,"yellow"),
    Rectangle(100,0,50,50,"yellow"),
    Rectangle(150,0,50,50,"yellow"),
    Rectangle(200,0,50,50,"yellow"),
    Rectangle(250,0,50,50,"yellow"),
    Rectangle(300,0,50,50,"yellow"),
    Rectangle(350,0,50,50,"yellow"),
    Rectangle(400,0,50,50,"yellow"),
    Rectangle(450,0,50,50,"yellow"),
    ]
bg.draw()
def Main(dt):
    for i in range(100):
        blocks[i].draw()
repeat(Main)
run()
