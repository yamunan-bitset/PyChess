import pygame
import pieces
from board import *

pygame.init()
(w, h) = (900, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Chess")

board = InitPieces(screen)
analysis = legal.Legal(board)

running = True
drag = (-1, -1)
select_pos1 = (-1, -1)
select_pos2 = (-1, -1)
found = False
while running:
    mouse = pygame.Vector2(pygame.mouse.get_pos())
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if drag[0] < 0:
            pos = get_pos_from_coord(mouse)
            for i in range(8):
                for j in range(8):
                    if board[i][j] != None:
                        if board[i][j].pos == pos:
                            drag = (i, j)
                            select_pos1 = pos
                            break
    if event.type == pygame.MOUSEBUTTONUP:
        if drag[0] >= 0:
            select_pos2 = get_pos_from_coord(mouse)
            board[drag[0]][drag[1]].pos = select_pos2
            board[drag[0]][drag[1]].coord = get_coord_from_pos(select_pos2)
            drag = (-1, -1)
            """
            for pos in analysis.legal(p[drag + 1].pos):
                found = False
                if pos == get_pos_from_coord(mouse):
                    for i in range(16, 32) if not analysis.white_turn else range(16):
                        if drag != i:
                            if p[i].pos == get_pos_from_coord(mouse):
                                print("captured", p[i].type, p[i].pos)
                                p[i].captured = True
                                break
                    analysis.board[select_pos1] = None
                    select_pos2 = get_pos_from_coord(mouse)
                    p[drag].pos = select_pos2
                    p[drag].coord = get_coord_from_pos(p[drag].pos)
                    analysis.board[select_pos2] = p[drag].type
                    drag = -1
                    analysis.white_turn = not analysis.white_turn
                    found = True
                    break
            if not found:
                p[drag].pos = select_pos1
                p[drag].coord = get_coord_from_pos(select_pos1)
                drag = -1
            """
    if drag[0] >= 0:
        board[drag[0]][drag[1]].coord = mouse - (50, 50)

    screen.fill((0, 0, 0))

    Board(screen)

    if select_pos1[0] >= 0:
        pygame.draw.rect(screen, (220, 190, 0), (get_coord_from_pos(select_pos1)[0], get_coord_from_pos(select_pos1)[1], 100, 100))
    if select_pos2[0] >= 0:
        pygame.draw.rect(screen, (220, 190, 0), (get_coord_from_pos(select_pos2)[0], get_coord_from_pos(select_pos2)[1], 100, 100))

    for i in range(8):
        for j in range(8):
            if board[i][j] != None:
                board[i][j].draw()
    pygame.display.update()