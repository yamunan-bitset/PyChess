import pygame
import pieces
from board import *
from copy import deepcopy

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Chess")

perfti = 0
start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
perft = [start_fen]
perft.append("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - ")
perft.append("8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - ")
perft.append("r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1")
perft.append("rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8  ")
perft.append("r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10 ")
board, turn = InitPieces(screen, perft[perfti])
analysis = legal.Legal(board, turn)

running = True
drag = (-2, -2)
select_pos1 = []
select_pos2 = []
found = False
board_buffer = 0
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
                    if analysis.board[i][j].type != "":
                        if analysis.board[i][j].type[:1] == ('w' if analysis.white_turn else 'b'):
                            if analysis.board[i][j].pos == pos:
                                drag = (i, j)
                                select_pos1.append(pos)
                                break
            print("Current pos:", select_pos1)
            try: print(analysis.legal(select_pos1[-1]))
            except: pass

    if event.type == pygame.MOUSEBUTTONUP:
        if drag[0] >= 0:
            if analysis.legal(select_pos1[-1]) != []:
                for pos in analysis.legal(select_pos1[-1])[0]:
                    if pos == get_pos_from_coord(mouse):
                        if analysis.legal(select_pos1[-1])[1] != None:
                            key = analysis.legal(select_pos1[-1])[1].split()
                            if pos == analysis.legal(select_pos1[-1])[0][int(key[1])]:
                                if key[0] == "entepassante":
                                    print("entepassante")
                                    analysis.board[int(key[2])][int(key[3])].type = ""
                                elif key[0] == "castle":
                                    if key[2] == 'k':
                                        if analysis.board[7][7 if analysis.white_turn else 0].type[2:] == "rook":
                                            col = "w_" if analysis.white_turn else "b_"
                                            analysis.board[5][7 if analysis.white_turn else 0].type = col + "rook"
                                            analysis.board[7][7 if analysis.white_turn else 0].type = ""
                                    elif key[2] == 'q':
                                        if analysis.board[0][7 if analysis.white_turn else 0].type[2:] == "rook":
                                            col = "w_" if analysis.white_turn else "b_"
                                            analysis.board[3][7 if analysis.white_turn else 0].type = col + "rook"
                                            analysis.board[0][7 if analysis.white_turn else 0].type = ""
                                    analysis.castled[0 if analysis.white_turn else 1] = True
                        analysis.history.append(pos)
                        p = analysis.board[select_pos1[-1][0]][select_pos1[-1][1]]
                        if analysis.castled[0 if analysis.white_turn else 1]:
                            if p.type[2:] == "rook":
                                print("\n\nReached\n\n")
                                if p.pos == (0, 0): analysis.q_rook_moved[1] = True
                                if p.pos == (0, 7): analysis.q_rook_moved[0] = True
                                if p.pos == (7, 0): analysis.k_rook_moved[1] = True
                                if p.pos == (7, 7): analysis.k_rook_moved[0] = True
                        analysis.board[select_pos1[-1][0]][select_pos1[-1][1]] = pieces.Piece(screen, "", select_pos1[-1])
                        select_pos2.append(get_pos_from_coord(mouse))
                        p.pos = select_pos2[-1]
                        p.coord = get_coord_from_pos(select_pos2[-1])
                        analysis.board[select_pos2[-1][0]][select_pos2[-1][1]] = p
                        drag = (-2, -2)
                        found = True
                        print(select_pos2[-1])
                        analysis.check = [False, (-2, -2)]
                        for check in analysis.legal(select_pos2[-1])[0]:
                            if analysis.board[check[0]][check[1]].type[2:] == "king":
                                analysis.check = [True, check]
                        analysis.white_turn = not analysis.white_turn
                        break
                analysis.board[select_pos1[-1][0]][select_pos1[-1][1]].pos = select_pos1[-1]
                analysis.board[select_pos1[-1][0]][select_pos1[-1][1]].coord = get_coord_from_pos(select_pos1[-1])
                drag = (-2, -2)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            try:
                p = analysis.board[select_pos2[-1][0]][select_pos2[-1][1]].type
                analysis.board[select_pos2[-1][0]][select_pos2[-1][1]].type = analysis.board[select_pos1[-1][0]][select_pos1[-1][1]].type
                analysis.board[select_pos1[-1][0]][select_pos1[-1][1]].type = p
                analysis.white_turn = not analysis.white_turn
                print(select_pos1)
                print(select_pos2)
                select_pos1 = select_pos1[:-1]
                select_pos2 = select_pos2[:-1]
                print(select_pos1)
                print(select_pos2)
            except IndexError:
                pass
        elif event.key == pygame.K_DOWN:
            try:
                perfti += 1
                board, turn = InitPieces(screen, perft[perfti])
                analysis.board = board
                analysis.white_turn = turn
            except IndexError:
                pass
        elif event.key == pygame.K_UP:
            try:
                perfti -= 1
                board, turn = InitPieces(screen, perft[perfti])
                analysis.board = board
                analysis.white_turn = turn
            except IndexError:
                pass

    screen.fill((0, 0, 0))
    Board(screen)

    if select_pos1 != [] and select_pos2 != []:
        pygame.draw.rect(screen, (220, 190, 0), (get_coord_from_pos(select_pos1[-1])[0], get_coord_from_pos(select_pos1[-1])[1], 100, 100))
        pygame.draw.rect(screen, (220, 190, 0), (get_coord_from_pos(select_pos2[-1])[0], get_coord_from_pos(select_pos2[-1])[1], 100, 100))

    if drag[0] >= 0:
        moves = analysis.legal(drag)
        for move in moves[0]:
            s = pygame.Surface((100, 100))
            s.set_alpha(200)
            s.fill((255, 0, 0))
            screen.blit(s, get_coord_from_pos(move))
        analysis.board[drag[0]][drag[1]].coord = mouse - BOARD_POS
        if get_pos_from_coord(mouse)[0] != -1 and get_pos_from_coord(mouse)[1] != -1:
            pygame.draw.rect(screen, (255, 255, 255), (get_coord_from_pos(get_pos_from_coord(mouse))[0], get_coord_from_pos(get_pos_from_coord(mouse))[1], 100, 100), 2)

    if analysis.check[0]:
        pygame.draw.rect(screen, (150, 0, 0), (get_coord_from_pos(analysis.check[1])[0], get_coord_from_pos(analysis.check[1])[1], 100, 100))

    for i in range(8):
        for j in range(8):
            if board[i][j] != None:
                board[i][j].draw()

    pygame.display.update()