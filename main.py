import pygame
import pieces
from board import *

pygame.init()
(w, h) = (900, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Chess")

start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board, turn = InitPieces(screen, start_fen)
analysis = legal.Legal(board, turn)

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
                    if analysis.board[i][j] != None:
                        if analysis.board[i][j].type[:1] == ('w' if analysis.white_turn else 'b'):
                            if analysis.board[i][j].pos == pos:
                                drag = (i, j)
                                select_pos1 = pos
                                break
            print("Current pos:", select_pos1)
            print(analysis.legal(select_pos1))

    if event.type == pygame.MOUSEBUTTONUP:
        if drag[0] >= 0:
            for pos in analysis.legal(select_pos1):
                found = False
                if pos == get_pos_from_coord(mouse):
                    p = analysis.board[select_pos1[0]][select_pos1[1]]
                    analysis.board[select_pos1[0]][select_pos1[1]] = None
                    select_pos2 = get_pos_from_coord(mouse)
                    p.pos = select_pos2
                    p.coord = get_coord_from_pos(select_pos2)
                    analysis.board[select_pos2[0]][select_pos2[1]] = p
                    drag = (-1, -1)
                    analysis.white_turn = not analysis.white_turn
                    print(select_pos2)
                    found = True
                    break
            if not found:
                analysis.board[select_pos1[0]][select_pos1[1]].pos = select_pos1
                analysis.board[select_pos1[0]][select_pos1[1]].coord = get_coord_from_pos(select_pos1)
                drag = (-1, -1)
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