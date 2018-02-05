import numpy as np
import subprocess
import random
import sys
import datetime

# boxchars: ╋ ━┃┣ ┫┳ ┻ ┛🡺🡻

test = ['a', 'b', 'c', '1', '2', '3']
player1 = 'abc'
player2 = '123'
darrow = '🡻'
rarrow = '🡺'

# goes_first = random.randint(0,1)
goes_first = 0
game_over = False

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


def main():
    player = goes_first
    # while (not game_over):
    render()
    main_phase(player)


def move_piece(player, piece):

    for i, val in enumerate(bs):
        try:
            row = val.index(piece)
            col = i
            break
        except ValueError:
            pass
    
    # coords for the piece to move
    print(col, row)
    
    if (player == 0):
        tmp = piece


    else:
        tmp = piece


    print(player, piece)


def main_phase(player):

    # if (player == 1):
    piece_to_move = input('Select a piece to move: ')
    move_piece(player, piece_to_move)



    player = (player + 1) % 2


main()

