from src.square import Square

class Turn():
    def __init__(self, store, game, user, row_num, col_num):
        self.id = len(store['turn'])
        self.token = user.token
        self.user_name = user.name
        store['turn'].append(self) 
        dim = store['dim']
        store['board'][game.board_id].squares[row_num*dim + col_num] =  Square(user.token)
