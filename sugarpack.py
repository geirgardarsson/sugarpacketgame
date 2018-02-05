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


def render(grid, player):
    subprocess.call('clear')
    sys.stdout.write(grid)
    sys.stdout.write('Player {0}\'s turn,'.format(player + 1))


def main(bs, grid, player):
    while (not game_over):
        render(grid, player)
        grid = main_phase(bs, player)
        player = (player + 1) % 2


def main_phase(bs, player):

    player_chars = player1 if player == 0 else player2

    while True:
        try:
            piece_to_move = input('\nSelect a piece to move (legal: {0} {1} {2}): '.format(*player_chars))
            if any(piece_to_move in i for i in player_chars):
                break
        except KeyboardInterrupt:
            sys.exit("\nexiting...")
        
    return move_piece(bs, player, piece_to_move)


def move_piece(bs, player, piece):

    for i, val in enumerate(bs):
        for j, k in enumerate(val):
            if k == rarrow or k == darrow:
                bs[i][j] = ' '

    for i, val in enumerate(bs):
        
        # finding the piece to move
        try:
            row = val.index(piece)
            col = i
            break
        except ValueError:
            pass
        
    jump = 1
    player_chars = player1 if player == 1 else player2
    
    if (player == 0):
        tmp = piece
        bs[col][row] = darrow

        for i in player_chars:
            if bs[col+jump][row] == i:
                jump += 1

        bs[col+jump][row] = tmp

    else:
        tmp = piece
        bs[col][row] = rarrow
        for i in player_chars:
            if bs[col][row+jump] == i:
                jump += 1

        bs[col][row+jump] = tmp

    newgrid = refresh(bs)
    return newgrid


grid = refresh(bs)
main(bs, grid, active_player)
