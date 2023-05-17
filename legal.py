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
        #print(self.board[pos[0]][pos[1]].type)
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

        if self.board[pos[0]][pos[1]].type[2:] == "rook":
            print("ROOOKIE REACHED")

        return moves
