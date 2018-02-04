import numpy as np
import subprocess

boxchars = '╋ ━┃┣ ┫┳ ┻ ┛'

test = ['a', 'b', 'c', '1', '2', '3']

grid = '   ┃ {0}   {1}   {2} ┃\n━━━╋━━━┳━━━┳━━━┫\n {3} ┃   ┃   ┃   ┃\n   ┣━━━╋━━━╋━━━┫\n {4} ┃   ┃   ┃   ┃\n   ┣━━━╋━━━╋━━━┫\n {5} ┃   ┃   ┃   ┃\n━━━┻━━━┻━━━┻━━━┛\n\n'.format(*test)

subprocess.call('clear')

def render():
    print(grid)


render()

