import pygame
import pieces
from board import *

pygame.init()
(w, h) = (900, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Chess")

p = list()
InitPieces(screen, p)

running = True
drag = -1
select_pos1 = -1
select_pos2 = -1
found = False
while running:
    mouse = pygame.Vector2(pygame.mouse.get_pos())
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if drag < 0:
            pos = pieces.get_pos_from_coord(mouse)
            for i in range(16, 32) if analysis.white_turn else range(16):
                if p[i].pos == pos:
                    drag = i
                    select_pos1 = pos
                    print(analysis.legal(p[i].pos))
                    break
    if event.type == pygame.MOUSEBUTTONUP:
        if drag > 0:
            for pos in analysis.legal(select_pos1):
                found = False
                if pos == pieces.get_pos_from_coord(mouse):
                    for i in range(16, 32) if not analysis.white_turn else range(16):
                        if drag != i:
                            if p[i].pos == pieces.get_pos_from_coord(mouse):
                                print("captured", p[i].type, p[i].pos)
                                p[i].captured = True
                                break
                    p[drag].pos = pieces.get_pos_from_coord(mouse)
                    p[drag].coord = pieces.get_coord_from_pos(p[drag].pos)
                    select_pos2 = pieces.get_pos_from_coord(mouse)
                    drag = -1
                    analysis.white_turn = not analysis.white_turn
                    found = True
                    break
            if not found:
                p[drag].pos = select_pos1
                p[drag].coord = pieces.get_coord_from_pos(select_pos1)
                drag = -1
    if drag > 0:
        p[drag].coord = mouse - (50, 50)

    screen.fill((0, 0, 0))
    Board(screen)
    if select_pos1 > 0:
        pygame.draw.rect(screen, (220, 190, 0), (pieces.get_coord_from_pos(select_pos1)[0], pieces.get_coord_from_pos(select_pos1)[1], 100, 100))
    if select_pos2 > 0:
        pygame.draw.rect(screen, (220, 190, 0), (pieces.get_coord_from_pos(select_pos2)[0], pieces.get_coord_from_pos(select_pos2)[1], 100, 100))

    for i in range(32):
        p[i].draw()
    pygame.display.update()