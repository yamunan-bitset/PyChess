class Legal:
    def __init__(self, board):
        self.board = board
        self.white_turn = True

    def legal(self, pos):
        moves = []
        if self.board[pos - 1][2:] == "pawn":
            if not self.white_turn:
                moves.append(pos + 8)
                if 9 <= pos <= 16:
                    moves.append(pos + 16)
            else:
                print("reached")
                moves.append(pos - 8)
                if 49 <= pos <= 56:
                    moves.append(pos - 16)

        return moves
