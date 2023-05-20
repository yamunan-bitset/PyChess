import board

class Legal:
    def __init__(self, board, turn):
        self.board = board
        print(turn)
        if turn == 'w':
            self.white_turn = True
        elif turn == 'b':
            self.white_turn = False
        self.history = []

    def legal(self, pos):
        moves = []
        special = None

        if self.board[pos[0]][pos[1]] == None:
            return moves

        if self.board[pos[0]][pos[1]].type[2:] == "pawn":
            moves, special = self.pawn_moves(pos)

        if self.board[pos[0]][pos[1]].type[2:] == "rook":
            moves = self.linear_sliding(pos)

        if self.board[pos[0]][pos[1]].type[2:] == "bishop":
            moves = self.diagonal_sliding(pos)

        if self.board[pos[0]][pos[1]].type[2:] == "queen":
            for move in self.linear_sliding(pos):
                moves.append(move)
            for move in self.diagonal_sliding(pos):
                moves.append(move)

        if self.board[pos[0]][pos[1]].type[2:] == "knight":
            moves = self.knight_moves(pos)

        if self.board[pos[0]][pos[1]].type[2:] == "king":
            moves, special = self.king_moves(pos)

        return moves, special

    def pawn_moves(self, pos):
        moves = []
        special = None

        if self.board[pos[0]][pos[1] + 1 if not self.white_turn else pos[1] - 1].type[:1] == "":
            moves.append((pos[0], pos[1] + 1 if not self.white_turn else pos[1] - 1))
        if self.white_turn:
            if pos[1] == 6:
                if self.board[pos[0]][pos[1] - 2].type == "" and self.board[pos[0]][pos[1] - 1].type == "":
                    moves.append((pos[0], pos[1] - 2))
            try:
                if self.board[pos[0] + 1][pos[1] - 1].type[:1] == 'b':
                    moves.append((pos[0] + 1, pos[1] - 1))
            except IndexError:
                pass
            try:
                if self.board[pos[0] - 1][pos[1] - 1].type[:1] == 'b':
                    moves.append((pos[0] - 1, pos[1] - 1))
            except IndexError:
                pass

        elif not self.white_turn:
            if pos[1] == 1:
                if self.board[pos[0]][pos[1] + 2].type == "" and self.board[pos[0]][pos[1] + 1].type == "":
                    moves.append((pos[0], pos[1] + 2))
            try:
                if self.board[pos[0] + 1][pos[1] + 1].type[:1] == 'w':
                    moves.append((pos[0] + 1, pos[1] + 1))
            except IndexError:
                pass
            try:
                if self.board[pos[0] - 1][pos[1] + 1].type[:1] == 'w':
                    moves.append((pos[0] - 1, pos[1] + 1))
            except IndexError:
                pass

        if (self.board[pos[0]][pos[1]].type[:1] == 'w' and pos[1] == 3) or (self.board[pos[0]][pos[1]].type[:1] == 'b' and pos[1] == 4):
            if self.board[self.history[-1][0]][self.history[-1][1]].type[2:] == "pawn":
                if (self.white_turn and self.board[self.history[-1][0]][self.history[-1][1]].type[:1] == 'b') or \
                        (not self.white_turn and self.board[self.history[-1][0]][self.history[-1][1]].type[:1] == 'w'):
                    if self.board[self.history[-1][0]][self.history[-1][1]].pos == (pos[0] - 1, pos[1]):
                        moves.append((pos[0] - 1, pos[1] - 1 if self.white_turn else pos[1] + 1))
                        special = f"entepassante {len(moves) - 1} {pos[0] - 1} {pos[1]}"
                    elif self.board[self.history[-1][0]][self.history[-1][1]].pos == (pos[0] + 1, pos[1]):
                        moves.append((pos[0] + 1, pos[1] - 1 if self.white_turn else pos[1] + 1))
                        special = f"entepassante {len(moves) - 1} {pos[0] + 1} {pos[1]}"

        return moves, special

    def linear_sliding(self, pos):
        moves = []
        for i in range(1, 8):
            m = (pos[0] + i, pos[1])
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0], pos[1] + i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0] - i, pos[1])
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0], pos[1] - i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        return moves

    def diagonal_sliding(self, pos):
        moves = []
        for i in range(1, 8):
            m = (pos[0] + i, pos[1] - i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0] - i, pos[1] + i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0] - i, pos[1] - i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        for i in range(1, 8):
            m = (pos[0] + i, pos[1] + i)
            if board.get_coord_from_pos(m) != (-1, -1):
                if self.board[m[0]][m[1]].type == "":
                    moves.append(m)
                else:
                    if (not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                            self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b'):
                        moves.append(m)
                        break
                    else:
                        break
        return moves

    def knight_moves(self, pos):
        moves = []
        m = (pos[0] + 1, pos[1] + 2)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] + 2, pos[1] + 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 1, pos[1] - 2)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 2, pos[1] - 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] + 1, pos[1] - 2)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 1, pos[1] + 2)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] + 2, pos[1] - 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 2, pos[1] + 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        return moves

    def king_moves(self, pos):
        moves = []
        special = None
        m = (pos[0] + 1, pos[1])
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 1, pos[1])
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0], pos[1] + 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0], pos[1] - 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] + 1, pos[1] - 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] + 1, pos[1] + 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 1, pos[1] + 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)
        m = (pos[0] - 1, pos[1] - 1)
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            if not ((self.white_turn and self.board[m[0]][m[1]].type[:1] == 'w') or (
                    not self.white_turn and self.board[m[0]][m[1]].type[:1] == 'b')):
                moves.append(m)

        m = (pos[0] + 2, pos[1])
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            try:
                if self.board[pos[0] + 1][pos[1]].type == "" and self.board[pos[0] + 2][pos[1]].type == "":
                    if self.board[pos[0] + 3][pos[1]].type[2:] == "rook":
                        moves.append(m)
                        special = f"castle {len(moves) - 1} k"
            except: pass
        m = (pos[0] - 2, pos[1])
        if not (m[0] > 7 or m[1] > 7 or m[0] < 0 or m[1] < 0):
            try:
                if self.board[pos[0] - 1][pos[1]].type == "" and self.board[pos[0] - 2][pos[1]].type == "" and self.board[pos[0] - 3][pos[1]].type == "":
                    if self.board[pos[0] - 4][pos[1]].type[2:] == "rook":
                        moves.append(m)
                        special = f"castle {len(moves) - 1} q"
            except: pass

        return moves, special
