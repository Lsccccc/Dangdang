from pyleap import *

window.set_size(500,500)

block_colors=[
    ['red','white','white','white','red','yellow','yellow','yellow','yellow','yellow'],
    ['red','red','white','white','red','yellow','white','white','white','yellow'],
    ['red','white','red','white','red','yellow','white','white','white','yellow'],
    ['red','white','white','red','red','yellow','white','white','white','yellow'],
    ['red','white','white','white','red','yellow','yellow','yellow','yellow','yellow'],
    ['blue','white','white','white','blue','green','green','green','green','green'],
    ['blue','blue','white','white','blue','green','white','white','white','white'],
    ['blue','white','blue','white','blue','green','green','green','green','green'],
    ['blue','white','white','blue','blue','green','white','white','white','white'],
    ['blue','white','white','white','blue','green','green','green','green','green']
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
