class Legal:
    def __init__(self, board):
        self.board = board
        self.white_turn = True

    def print_board(self):
        print()
        for i in range(64):
            if i % 8 == 7:
                print(str(self.board[i]) + ' ')
            else:
                print(self.board[i], end=" ")

    def legal(self, pos):
        moves = []
        if self.board[pos] == None:
            return moves

        if self.board[pos][2:] == "pawn":
            moves.append(pos + 7 if not self.white_turn else pos - 7)
            if not self.white_turn:
                if 9 <= pos <= 16:
                    moves.append(pos + 15)
            else:
                if 49 <= pos <= 56:
                    moves.append(pos - 15)
        if self.board[pos][2:] == "rook":
            print("ROOOKIE REACHED")

        return moves
