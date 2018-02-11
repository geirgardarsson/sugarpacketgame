import subprocess
import random
import sys
from datetime import datetime
from time import sleep
import copy

# boxchars: ╋ ━┃┣ ┫┳ ┻ ┛🡺🡻

g_player1 = ['a', 'b', 'c']
g_player2 = ['1', '2', '3']
g_p1_finished = []
g_p2_finished = []
darrow = '🡻'
rarrow = '🡺'

goes_first = random.randint(0,1)

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
        if (len(g_p1_finished) == 3 or len(g_p2_finished) == 3):
            break
        bs = main_phase(bs, player, g_p1_finished, g_p2_finished)
        grid = refresh(bs)
        player = (player + 1) % 2
    
    sys.exit('\n\n Player {} won!\n'.format(str(player + 1)))


def main_phase(bs, player, p1_finished, p2_finished):
    legal_moves = find_legal_moves(bs, player)

    if not legal_moves:
                print('\nNo legal moves, passing turn...')
                sleep(3)
                return move_piece(bs, player, False, p1_finished, p2_finished)

    if player == 0:
        
        if len(legal_moves) == 1:
            return move_piece(bs, player, legal_moves[0], p1_finished, p2_finished)        

        t1 = datetime.now()

        # copy our data by value so the calculations won't mess up the actual game state
        dummy_bs = copy.deepcopy(bs)
        p1_tmp = list(p1_finished)
        p2_tmp = list(p2_finished)
        p = copy.deepcopy(player)

        piece = calc_main(dummy_bs, player, p1_tmp, p2_tmp)
        print('piece', piece)

        # move = max(potential_moves, key=lambda item:item[1])    
        t2 = datetime.now()
        total = t2 - t1
        sys.stdout.write('\nSelected to move ' + str(piece) + ', in ' + str(total))

        return move_piece(bs, player, piece, p1_finished, p2_finished)
        
    else:   
        while True:
            try:
                piece_to_move = input('\nSelect a piece to move (legal: {0}): '.format(' '.join(legal_moves)))
                if piece_to_move == '':
                    continue
                if (piece_to_move in legal_moves):
                    break
            except KeyboardInterrupt:
                sys.exit("\nexiting...")
        
    return move_piece(bs, player, piece_to_move, p1_finished, p2_finished)


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
        legal_moves = list(set(legal_moves) - set(g_p1_finished))

    else:
        for p in range(len(g_player2)):
            char = g_player2[p]
            index = bs[p+1].index(char)
            if index < 2:
                onestep = bs[p+1][index+1]
                twostep = bs[p+1][index+2]
                if (onestep in g_player1 and twostep in g_player1):
                    legal_moves.remove(char)

        legal_moves = list(set(legal_moves) - set(g_p2_finished))

    legal_moves.sort()
    return legal_moves


def move_piece(bs, player, piece, p1_finished, p2_finished):
    if not piece:
        return bs

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
        if col+jump > 3:
            p1_finished.append(tmp)

    else:
        tmp = piece
        bs[col][row] = rarrow
        for i in player_chars:
            if bs[col][row+jump] == i:
                jump += 1

        bs[col][row+jump] = tmp
        if row+jump > 3:
            p2_finished.append(tmp)

    return bs


def calc_main(bs, player, p1, p2):

    legal_moves = list(set(g_player1) - set(p1)) if player == 0 else list(set(g_player2) - set(p2))

    print('\n\n', legal_moves, '\n\n')

    potential_moves = []

    for i in legal_moves:
        tmp_bs = copy.deepcopy(bs)
        tmp_player = copy.deepcopy(player)
        tmp_p1 = list(p1)
        tmp_p2 = list(p2)

        value = calc(tmp_bs, tmp_player, i, tmp_p1, tmp_p2)

        potential_moves.append((i, value))

    print(potential_moves)
    move = max(potential_moves, key=lambda item:item[1])

    return move[0]


def calc(bs, player, piece, p1, p2):

    tmp_bs = move_piece(bs, player, piece, p1, p2)
    
    if len(p1) == 3:
        return 1

    if len(p2) == 3:
        return -1

    tmp_player = copy.deepcopy(player)
    tmp_player = (tmp_player + 1) % 2      

    legal_moves = list(set(g_player1) - set(p1)) if tmp_player == 0 else list(set(g_player2) - set(p2))
    value = 0

    for i in legal_moves:
        tmp_bs = copy.deepcopy(bs)
        tmp_p1 = list(p1)
        tmp_p2 = list(p2)
        
        value += calc(tmp_bs, tmp_player, i, tmp_p1, tmp_p2)

    return value


grid = refresh(bs)
main(bs, grid, goes_first)
