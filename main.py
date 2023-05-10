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
drag = 0
while running:
    mouse = pygame.Vector2(pygame.mouse.get_pos())
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if drag == 0:
            pos = pieces.get_pos_from_coord(mouse)
            for i in range(32):
                if p[i].pos == pos:
                    drag = i
                    break
    if event.type == pygame.MOUSEBUTTONUP:
        if drag > 0:
            for i in range(32):
                if drag != i:
                    if p[i].pos == p[drag].pos:
                        print("captured", p[i].type, p[i].pos)
                        p[i].captured = True
                        break
            p[drag].pos = pieces.get_pos_from_coord(mouse)
            p[drag].coord = pieces.get_coord_from_pos(p[drag].pos)
            drag = 0
    if drag > 0:
        p[drag].coord = mouse - (50, 50)

    screen.fill((0, 0, 0))
    Board(screen)
    for i in range(32):
        if not p[i].captured:
            p[i].draw()
    pygame.display.update()