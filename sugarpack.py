import numpy as np
import subprocess
import random
import sys
import datetime

# boxchars: ╋ ━┃┣ ┫┳ ┻ ┛🡺🡻

player1 = ['a', 'b', 'c']
player2 = ['1', '2', '3']
darrow = '🡻'
rarrow = '🡺'

active_player = random.randint(0,1)
game_over = False

# Boardstate
bs = ([[' ', 'a', 'b', 'c', ' '],
       ['1', ' ', ' ', ' ', ' '],
       ['2', ' ', ' ', ' ', ' '],
       ['3', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']])


def refresh(bs):

    row0 = ' {0} ┃ {1}   {2}   {3} ┃ {4}\n━━━╋━━━┳━━━┳━━━┫\n'.format(*bs[0])
    row1 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n   ┣━━━╋━━━╋━━━┫\n'.format(*bs[1])
    row2 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n   ┣━━━╋━━━╋━━━┫\n'.format(*bs[2])
    row3 = ' {0} ┃ {1} ┃ {2} ┃ {3} ┃ {4}\n━━━┻━━━┻━━━┻━━━┛\n'.format(*bs[3])
    row4 = ' {0}   {1}   {2}   {3}   {4}\n'.format(*bs[4])

    grid = row0 + row1 + row2 + row3 + row4
    return grid


def render(grid):
    subprocess.call('clear')
    print(grid)
    print('Player {0}\'s turn,'.format(active_player + 1))


def main(grid, player):
    # while (not game_over):
    render(grid)
    main_phase(player)


def main_phase(player):

    player_chars = player1 if player == 0 else player2

    # if (player == 1):
    while True:
        piece_to_move = input('Select a piece to move (legal: {0} {1} {2}): '.format(*player_chars))
        if any(piece_to_move in i for i in player_chars):
            break
        
    move_piece(player, piece_to_move)
    player = (player + 1) % 2


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
        bs[col][row] = darrow
        bs[col+1][row] = tmp

    else:
        tmp = piece
        bs[col][row] = rarrow
        bs[col][row+1] = tmp

    newgrid = refresh(bs)
    render(newgrid)


grid = refresh(bs)
main(grid, active_player)

