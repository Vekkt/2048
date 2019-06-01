from board import *
from math import log2

def convert(board):
    mat = board.getBoard()
    val = 0
    for i in range(4):
        for j in range(4):
            shift = 60 - i * 16 + j * 4
            power = int(log2(mat[i][j]))
            val += (bin(power) << shift)
    return val

def value(board):
    # todo
    return 0

def step(board, move):
    # todo
    return board

def compute(board, depth, moves = []):
    if depth == 0:
        return (value(board), moves)
    else:
        max_b = 0
        max_val = 0
        max_mov = moves

        move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for move in move_list:
            if not moves or move != moves[-1]:
                val, movs, b = compute(
                    step(board, move), 
                    depth - 1, 
                    moves.copy() + [move])

                if val > max_val:
                    max_b = b
                    max_val = val
                    max_mov = movs

        return (max_val, max_mov, max_b)

