from pyleap import *

window.set_size(500,500)

block_colors=[
    ['purple','purple','purple','purple','purple','purple','purple','purple','purple','purple'],
    ['purple','purple','purple','purple','red','red','purple','purple','purple','purple'],
    ['purple','purple','purple','red','red','red','red','purple','purple','purple'],
    ['purple','purple','red','red','red','red','red','red','purple','purple'],
    ['purple','red','red','red','red','red','red','red','red','purple'],
    ['purple','purple','purple','purple','red','red','purple','purple','purple','purple'],
    ['purple','purple','purple','purple','red','red','purple','purple','purple','purple'],
    ['purple','purple','purple','purple','red','red','purple','purple','purple','purple'],
    ['purple','purple','purple','purple','red','red','purple','purple','purple','purple'],
    ['purple','purple','purple','purple','purple','purple','purple','purple','purple','purple']
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
