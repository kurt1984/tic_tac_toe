class Game():
    def __init__(self, store, board, users) -> None:
        self.id = len(store['game'])
        self.players = users
        self.board_id = board.id
        self.store = store
        store['game'].append(self)

    def win_combo(self):
        dim = self.store["dim"]
        win_row = [list(range(i*dim, i*dim+dim)) for i in range(dim)]
        win_col = [list(range(i, i+dim*dim, dim)) for i in range(dim)]
        win_diag = [list(range(0, dim**2, dim+1)), list(range(dim-1, dim**2-1, dim-1))]
        return win_row + win_col + win_diag

    def win(self):
        for win_cond in self.win_combo():
            check_set = set([self.store["board"][self.board_id].squares[index].value for index in win_cond])
            if len(check_set) == 1 and check_set != {""}:
                winner_name = self.players[0].name if self.players[0].token == list(check_set)[0] else self.players[1].name
                return f'Player: {winner_name} wins! who played {list(check_set)[0]}'
        return None

    def board_full(self):
        return not ("" in self.store['board'][self.board_id].get_squares_token())
    
    def game_status(self):
        win_y = self.win()
        if win_y: 
            return 1, win_y
        elif self.board_full():
            return 2, "Board is full. It is a tie!"
        else:
            return 3, "Please continue..."
