import pygame
import pieces
import legal

def get_pos_from_coord(coord):
    if 50 <= coord[0] < 150: x = 0
    if 150 <= coord[0] < 250: x = 1
    if 250 <= coord[0] < 350: x = 2
    if 350 <= coord[0] < 450: x = 3
    if 450 <= coord[0] < 550: x = 4
    if 550 <= coord[0] < 650: x = 5
    if 650 <= coord[0] < 750: x = 6
    if 750 <= coord[0] < 850: x = 7

    if 50 <= coord[1] < 150: y = 0
    if 150 <= coord[1] < 250: y = 1
    if 250 <= coord[1] < 350: y = 2
    if 350 <= coord[1] < 450: y = 3
    if 450 <= coord[1] < 550: y = 4
    if 550 <= coord[1] < 650: y = 5
    if 650 <= coord[1] < 750: y = 6
    if 750 <= coord[1] < 850: y = 7

    return (x, y)

def get_coord_from_pos(pos):
    return (50 + pos[0] * 100, 50 + pos[1] * 100)

BOARD_POS = (50, 50)
size = 100
length = 8
board = [[None] * 8] * 8

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

def InitPieces(screen):
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)

    board[0][0] = pieces.Piece(screen, "b_rook", (0, 0))
    board[7][0] = pieces.Piece(screen, "b_rook", (7, 0))
    board[1][0] = pieces.Piece(screen, "b_knight", (1, 0))
    board[6][0] = pieces.Piece(screen, "b_knight", (6, 0))
    board[2][0] = pieces.Piece(screen, "b_bishop", (2, 0))
    board[5][0] = pieces.Piece(screen, "b_bishop", (5, 0))
    board[4][0] = pieces.Piece(screen, "b_king", (4, 0))
    board[3][0] = pieces.Piece(screen, "b_queen", (3, 0))

    board[0][7] = pieces.Piece(screen, "w_rook", (0, 7))
    board[7][7] = pieces.Piece(screen, "w_rook", (7, 7))
    board[1][7] = pieces.Piece(screen, "w_knight", (1, 7))
    board[6][7] = pieces.Piece(screen, "w_knight", (6, 7))
    board[2][7] = pieces.Piece(screen, "w_bishop", (2, 7))
    board[5][7] = pieces.Piece(screen, "w_bishop", (5, 7))
    board[4][7] = pieces.Piece(screen, "w_king", (4, 7))
    board[3][7] = pieces.Piece(screen, "w_queen", (3, 7))

    for x in range(0, 8):
        board[x][1] = pieces.Piece(screen, "b_pawn", (x, 1))
        board[x][6] = pieces.Piece(screen, "w_pawn", (x, 6))

    return board
