from pyleap import *

window.set_size(500,500)

block_colors=[
    ['indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo'],
    ['indigo','indigo','indigo','orange','green','green','orange','indigo','indigo','indigo'],
    ['indigo','indigo','orange','green','green','green','green','orange','indigo','indigo'],
    ['indigo','indigo','green','green','green','green','green','green','indigo','indigo'],
    ['indigo','green','green','green','green','green','green','green','green','indigo'],
    ['indigo','indigo','orange','brown','green','green','brown','orange','indigo','indigo'],
    ['indigo','indigo','orange','brown','green','green','brown','orange','indigo','indigo'],
    ['indigo','indigo','indigo','orange','green','green','orange','indigo','indigo','indigo'],
    ['indigo','indigo','indigo','indigo','orange','orange','indigo','indigo','indigo','indigo'],
    ['indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo']
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
