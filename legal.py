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
        if self.board[pos[0]][pos[1]] == None:
            return moves
        print(self.board[pos[0]][pos[1]].type)
        if self.board[pos[0]][pos[1]].type[2:] == "pawn":
            moves.append((pos[0], pos[1] + 1 if not self.white_turn else pos[1] - 1))
            if self.white_turn:
                if pos[1] == 6:
                    moves.append((pos[0], pos[1] - 2))
            else:
                if pos[1] == 1:
                    moves.append((pos[0], pos[1] + 2))
        if self.board[pos[0]][pos[1]].type[2:] == "rook":
            print("ROOOKIE REACHED")

        return moves
