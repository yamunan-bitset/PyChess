import pygame
import pieces

BOARD_POS = (50, 50)
size = 100
length = 8

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
        p.append(pieces.Piece(screen, f"{col}_{piece}", i + 1 if 0 <= i < 16 else 80 - i))
