from pyleap import *

window.set_size(500,500)

block_colors=[
    ['red','red','red','red','red','red','red','red','red','red'],
    ['red','red','red','red','red','red','red','gold','gold','red'],
    ['red','red','red','red','red','red','gold','gold','gold','red'],
    ['red','red','red','red','red','gold','gold','gold','red','red'],
    ['red','red','red',(255,255,80),'gold','gold','gold','red','red','red'],
    ['red','red',(255,255,80),(255,255,80),'gold','gold','red','red','red','red'],
    ['red',(255,255,80),(255,255,80),(255,255,80),(255,255,80),(255,255,80),'red','red','red','red'],
    [(255,255,80),(255,255,80),(255,255,80),(255,255,80),(255,255,80),'red','red','red','red','red'],
    [(255,255,80),(255,255,80),(255,255,80),(255,255,80),'red','red','red','red','red','red'],
    [(255,255,80),(255,255,80),(255,255,80),'red','red','red','red','red','red','red']
    ]

blocks=[]

for X in range(10):
    for Y in range(10):
        blocks.append(Rectangle(X*50,450-Y*50,50,50,block_colors[Y][X]))
    
def Main(dt):
    window.clear()
    for block in blocks:
        block.draw()

repeat(Main)
run()
