import numpy as np
import subprocess

boxchars = '╋ ━┃┣ ┫┳ ┻ ┛'

test = ['a', 'b', 'c', '1', '2', '3']

# Boardstate
bs = ([[' ', 'a', 'b', 'c', ' '],
       ['1', ' ', ' ', ' ', ' '],
       ['2', ' ', ' ', ' ', ' '],
       ['3', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']])


row0 = ' {0} ┃ {1}   {2}   {3} ┃ {4}\n━━━╋━━━┳━━━┳━━━┫\n'.format(*bs[0])
row1 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n   ┣━━━╋━━━╋━━━┫\n'.format(*bs[1])
row2 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n   ┣━━━╋━━━╋━━━┫\n'.format(*bs[2])
row3 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n━━━┻━━━┻━━━┻━━━┛\n'.format(*bs[3])
row4 = ' {0}   {1}   {2}   {3}   {4}\n'.format(*bs[4])

grid = row0 + row1 + row2 + row3 + row4

def render():
    subprocess.call('clear')
    print(grid)
    print(bs)


render()

