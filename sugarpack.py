import numpy as np
import subprocess
import random
import sys
import datetime

# boxchars: ╋ ━┃┣ ┫┳ ┻ ┛🡺🡻

g_player1 = ['a', 'b', 'c']
g_p1_finished = []
g_player2 = ['1', '2', '3']
g_p2_finished = []
darrow = '🡻'
rarrow = '🡺'

goes_first = random.randint(0,1)
g_game_over = False

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
    # subprocess.call('clear')
    sys.stdout.write(grid)
    sys.stdout.write('Player {0}\'s turn,'.format(player + 1))


def main(bs, grid, player):
    while True:
        render(grid, player)
        print(len(g_p1_finished), len(g_p2_finished))        
        grid = main_phase(bs, player)
        if (len(g_p1_finished) == 3 or len(g_p2_finished) == 3):
            break
            print(g_game_over)
        else:
            player = (player + 1) % 2
    
    sys.exit('\n Player {} won!'.format(str(player + 1)))


def main_phase(bs, player):

    legal_moves = find_legal_moves(bs, player)

    while True:
        try:
            piece_to_move = input('\nSelect a piece to move (legal: {0}): '.format(' '.join(legal_moves)))
            if piece_to_move == '':
                continue
            if (piece_to_move in legal_moves):
                break
        except KeyboardInterrupt:
            sys.exit("\nexiting...")
        
    return move_piece(bs, player, piece_to_move)


def find_legal_moves(bs, player):
    
    legal_moves = list(g_player1) if player == 0 else list(g_player2)

    if player == 0:
        for p in range(len(g_player1)):
            # -3 because we don't need to check the far end
            for i in range(len(bs)-3):
                char = g_player1[p]
                # Pieces can't move if there are two pieces infront
                if (any(char in j for j in bs[i])):
                    onestep = bs[i+1][p+1]
                    twostep = bs[i+2][p+1]
                    if (onestep in g_player2 and twostep in g_player2):
                        legal_moves.remove(char)
        
        # pieces that have finished
        lastrow = bs[-1]
        for i in lastrow[1:-1]:
            if i != ' ':
                legal_moves.remove(i)
                if i not in g_p1_finished:
                    g_p1_finished.append(i)

    else:
        # similar to above but inverted
        for p in range(len(g_player2)):
            for i in range(len(bs)-3):
                char = g_player2[p]
                if (any(char in j for j in bs[i])):
                    onestep = bs[p+1][i+1]
                    twostep = bs[p+1][i+2]
                    if (onestep in g_player1 and twostep in g_player1):
                        legal_moves.remove(char)

        # goodbye scalability
        lastcol = list([bs[1][-1], bs[2][-1], bs[3][-1]])
        for i in lastcol:
            if i != ' ':
                legal_moves.remove(i)
                if i not in g_p2_finished:
                    g_p2_finished.append(i)

    print(g_p1_finished, g_p2_finished) 
    return legal_moves


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
    player_chars = g_player1 if player == 1 else g_player2
    
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
main(bs, grid, goes_first)
