import pygame
import pieces
import legal

def get_pos_from_coord(coord):
    x = -1
    y = -1
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
    m = (50 + pos[0] * 100, 50 + pos[1] * 100)
    if m[0] > 750 or m[1] > 750 or m[0] < 50 or m[1] < 50:
        return (-1, -1)
    return m

BOARD_POS = (50, 50)
size = 100
length = 8
board = [[None] * 8] * 8

def Board(screen):
    cnt = 0
    for i in range(length):
        for j in range(length):
            if cnt % 2 == 0:
                pygame.draw.rect(screen, (241, 217, 192), [size * j + BOARD_POS[0], size * i + BOARD_POS[1], size, size])
            else:
                pygame.draw.rect(screen, (169, 122, 101), [size * j + BOARD_POS[0], size * i + BOARD_POS[1], size, size])
            cnt += 1
        cnt -= 1
    pygame.draw.rect(screen, (120, 0, 0), [25, 25, length * size + BOARD_POS[0], length * size + BOARD_POS[0]], 20)

def InitPieces(screen, fen):
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(pieces.Piece(screen, "", (y, x)))
    t = ""
    turn = ''
    xiter = 0
    yiter = 0
    check_turn = False
    check_castle = False
    for i in fen:
        for j in i:
            print(j, xiter)
            if check_turn:
                print("Turn", j)
                turn = j
                check_turn = False
                break
            if check_castle: # TODO
                #check_castle = False
                break
            elif j == ' ':
                if turn == '':
                    if not check_turn:
                        check_turn = True
                else:
                    check_castle = True
                break
            elif j == '/':
                print("reached slash")
                yiter += 1
                if xiter == 8:
                    xiter = 0
            elif j.isdigit():
                print("reached is digit:", j)
                print("xiter before", xiter)
                xiter += int(j) % 8
                print("xiter:",xiter)
            else:
                if j == 'r':
                    t = "b_rook"
                elif j == 'R':
                    t = "w_rook"
                elif j == 'k':
                    t = "b_king"
                elif j == 'K':
                    t = "w_king"
                elif j == 'p':
                    t = "b_pawn"
                elif j == 'P':
                    t = "w_pawn"
                elif j == 'n':
                    t = "b_knight"
                elif j == 'N':
                    t = "w_knight"
                elif j == 'b':
                    t = "b_bishop"
                elif j == 'B':
                    t = "w_bishop"
                elif j == 'q':
                    t = "b_queen"
                elif j == 'Q':
                    t = "w_queen"
                print("x, y:", xiter, yiter)
                board[xiter][yiter] = pieces.Piece(screen, t, (xiter, yiter))
                xiter += 1
                if xiter == 8:
                    xiter = 0
    return board, turn