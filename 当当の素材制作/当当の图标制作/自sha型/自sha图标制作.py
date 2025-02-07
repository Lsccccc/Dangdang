from pyleap import *

window.set_size(500,500)

block_colors=[
    ['black','black','black','black','black','black','black','brown','brown','brown'],
    ['black','black','black','black','black','black','brown','brown','brown','brown'],
    ['black','black','black','black','black','brown','brown','brown','brown','brown'],
    ['black','black','black','black','brown','brown','brown','brown','brown','black'],
    ['black','black','black','black','gray','gray','brown','brown','black','black'],
    ['black','black','black','gray','gray','gray','brown','black','black','black'],
    ['black','black','gray','gray','gray','black','black','black','black','black'],
    ['black','gray','gray','gray','black','black','black','black','black','black'],
    ['black','gray','gray','black','black','black','black','black','black','black'],
    ['black','black','black','black','black','black','black','black','black','black']
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
