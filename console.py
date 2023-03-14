
from src.tictactoe import TicTacToe
from src.store import store
from src.user import User
from src.turn import Turn


users = []
tokens = ["X", "O"]
dim = int(input("tic-tac-toe game dim: "))

for i in range(2):
    if input(f"Is player {i} a bot [y/n]") == "y":
        users.append(User(store, name = "bot", token = tokens[i], bot= True))
    else:
        name = input(f"your name for player {i}:")
        users.append(User(store, name = name, token = tokens[i], bot = False))

# game_ttt = TicTacToe(
#     store=store, squares=squares_Owin_in_a_row, user1=user1, user2=user2
# )

# print(game_ttt.game.win())

game_ttt = TicTacToe(
    store=store, users = users, dim = dim
)


# Turn(store, game = game_ttt.game, user = user1, row_num = 0, col_num = 0)
# breakpoint()
# print(game_ttt.board.get_squares_token())



def make_turn(store, game, user, row_num, col_num):
    Turn(store, game = game, user = user, row_num = row_num, col_num = col_num)
    game_ttt.board.display_board()
    status, output = game_ttt.game.game_status()
    print(output)
    if int(status) in [1,2]:
        raise StopIteration


def player_move(user):
    row_num = int(input(f'{user.name} play: row: '))-1
    col_num = int(input(f'{user.name} play: column: '))-1
    make_turn(store, game_ttt.game, user, row_num, col_num)


def main_two_players():
    try:
        while True:
            for user in users:
                player_move(user)
    except StopIteration:
        pass

def main_bot():
    try:
        while True:
            for user in users:
                if user.bot:
                    row_num, col_num = user.bot_random_move(store, game_ttt)
                    make_turn(store, game_ttt.game, user, row_num, col_num)

                else:
                    player_move(user)

    except StopIteration:
        pass

if __name__ == "__main__":
    if True in [user.bot for user in users]:
        main_bot()
    else:
        main_two_players()
