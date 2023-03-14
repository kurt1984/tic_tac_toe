class User():
    def __init__(self, store, name, token, bot) -> None:
        self.id = len(store['user'])
        self.name = name
        self.token = token
        self.bot = bot
        store['user'].append(self)

    @staticmethod
    def bot_random_move(store, tictactoe_game):
        import random
        tokens = store['board'][tictactoe_game.game.board_id].get_squares_token()
        index_empty_tokens = [i for i, token in enumerate(tokens) if token == ""] 
        random_index_token = random.choice(index_empty_tokens)
        dim = store['dim']
        return divmod(random_index_token, dim)