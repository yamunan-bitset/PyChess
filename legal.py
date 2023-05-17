import board

class Legal:
    def __init__(self, board, turn):
        self.board = board
        print(turn)
        if turn == 'w': self.white_turn = True
        elif turn == 'b': self.white_turn = False


    def print_board(self):
        print()
        for i in range(64):
            if i % 8 == 7:
                print(str(self.board[i]) + ' ')
            else:
                print(self.board[i], end=" ")

    def legal(self, pos):
        moves = []
        if self.board[pos[0]][pos[1]] == None:
            return moves

        # Pawn
        if self.board[pos[0]][pos[1]].type[2:] == "pawn":
            if self.board[pos[0]][pos[1] + 1 if not self.white_turn else pos[1] - 1].type[:1] == "":
                moves.append((pos[0], pos[1] + 1 if not self.white_turn else pos[1] - 1))
            if self.white_turn:
                if pos[1] == 6:
                    moves.append((pos[0], pos[1] - 2))
                try:
                    if self.board[pos[0] + 1][pos[1] - 1].type[:1] == 'b':
                        moves.append((pos[0] + 1, pos[1] - 1))
                except IndexError: pass
                try:
                    if self.board[pos[0] - 1][pos[1] - 1].type[:1] == 'b':
                        moves.append((pos[0] - 1, pos[1] - 1))
                except IndexError: pass

            elif not self.white_turn:
                if pos[1] == 1:
                    moves.append((pos[0], pos[1] + 2))
                try:
                    if self.board[pos[0] + 1][pos[1] + 1].type[:1] == 'w':
                        moves.append((pos[0] + 1, pos[1] + 1))
                except IndexError: pass
                try:
                    if self.board[pos[0] - 1][pos[1] + 1].type[:1] == 'w':
                        moves.append((pos[0] - 1, pos[1] + 1))
                except IndexError: pass

        # Rook
        if self.board[pos[0]][pos[1]].type[2:] == "rook":
            for i in range(1, 8):
                m = (pos[0] + i, pos[1])
                if board.get_coord_from_pos(m) != (-1, -1):
                    if self.board[m[0]][m[1]].type == "":
                        moves.append(m)
                    else:
                        if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                            moves.append(m)
                            break
            for i in range(1, 8):
                m = (pos[0], pos[1] + i)
                if board.get_coord_from_pos(m) != (-1, -1):
                    if self.board[m[0]][m[1]].type == "":
                        moves.append(m)
                    else:
                        if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                            moves.append(m)
                            break
            for i in range(1, 8):
                m = (pos[0] - i, pos[1])
                if board.get_coord_from_pos(m) != (-1, -1):
                    if self.board[m[0]][m[1]].type == "":
                        moves.append(m)
                    else:
                        if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                            moves.append(m)
                            break
            for i in range(1, 8):
                m = (pos[0], pos[1] - i)
                if board.get_coord_from_pos(m) != (-1, -1):
                    if self.board[m[0]][m[1]].type == "":
                        moves.append(m)
                    else:
                        if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                            moves.append(m)
                            break

        return moves
