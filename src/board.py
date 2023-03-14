from src.square import Square

class Board():
    def __init__(self, store) -> None:
        self.store = store
        self.id = len(store['board'])
        store['board'].append(self)

    def get_squares_token(self):
        return [square.value for square in self.store['board'][self.id].squares]
    
    def display_board(self):
        dim = self.store["dim"]
        for i in range(dim):
            print(self.get_squares_token()[i*dim:i*dim+dim])

    
