
from src.square import Square
from src.board import Board
from src.game import Game

class TicTacToe():

    def __init__(self, store, users, dim, squares = None):
        self.board = Board(store)
        store['dim'] = dim
        self.board.squares = self.build_board(squares, dim)
        self.users = users
        self.game = Game(store, self.board, self.users)

    def build_board(self, squares, dim):
        if squares is None:
            squares = [Square("") for _ in range(dim ** 2)]
        return squares


