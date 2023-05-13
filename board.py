import pygame
import pieces
import legal

def get_pos_from_coord(coord):
    if 50 <= coord[0] < 150: x = 1
    if 150 <= coord[0] < 250: x = 2
    if 250 <= coord[0] < 350: x = 3
    if 350 <= coord[0] < 450: x = 4
    if 450 <= coord[0] < 550: x = 5
    if 550 <= coord[0] < 650: x = 6
    if 650 <= coord[0] < 750: x = 7
    if 750 <= coord[0] < 850: x = 8

    if 50 <= coord[1] < 150: y = 0
    if 150 <= coord[1] < 250: y = 1
    if 250 <= coord[1] < 350: y = 2
    if 350 <= coord[1] < 450: y = 3
    if 450 <= coord[1] < 550: y = 4
    if 550 <= coord[1] < 650: y = 5
    if 650 <= coord[1] < 750: y = 6
    if 750 <= coord[1] < 850: y = 7

    try:
        return (x % 9) + y * 8
    except UnboundLocalError:
        return -1

def get_coord_from_pos(pos):
    y = 0
    if 8 >= pos > 0: y = 0
    if 16 >= pos > 8: y = 1
    if 24 >= pos > 16: y = 2
    if 32 >= pos > 24: y = 3
    if 40 >= pos > 32: y = 4
    if 48 >= pos > 40: y = 5
    if 56 >= pos > 48: y = 6
    if 64 >= pos > 56: y = 7
    ret = (((pos - 1) % 8) * 100 + 50, y * 100 + 50)
    return ret

BOARD_POS = (50, 50)
size = 100
length = 8
board = [None] * 64

def Board(screen):
    cnt = 0
    for i in range(length):
        for j in range(length):
            if cnt % 2 == 0:
                pygame.draw.rect(screen, (245, 220, 190), [size * j + BOARD_POS[0], size * i + BOARD_POS[1], size, size])
            else:
                pygame.draw.rect(screen, (154, 87, 26), [size * j + BOARD_POS[0], size * i + BOARD_POS[1], size, size])
            cnt += 1
        cnt -= 1
    pygame.draw.rect(screen, (120, 0, 0), [25, 25, length * size + BOARD_POS[0], length * size + BOARD_POS[0]], 20)

def InitPieces(screen, p):
    for i in range(32):
        if i < 16:
            col = 'b'
        else:
            col = 'w'
        piece = "queen"
        if (8 <= i < 16 or 24 <= i < 32):
            piece = "pawn"
        elif (i == 0 or i == 7 or i == 16 or i == 23):
            piece = "rook"
        elif (i == 1 or i == 6 or i == 17 or i == 22):
            piece = "knight"
        elif (i == 2 or i == 5 or i == 18 or i == 21):
            piece = "bishop"
        elif (i == 4 or i == 19):
            piece = "king"
        board[i if col == 'b' else (80 - i) - 1] = col + "_" + piece
        p.append(pieces.Piece(screen, f"{col}_{piece}", i + 1 if 0 <= i < 16 else 80 - i))
