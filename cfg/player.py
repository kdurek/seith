import puzzles.numberguess


class Player:
    def __init__(self):
        self.name = 'Duras'


my_player = Player()

puzzles.numberguess.main_loop(my_player.name)


def bacon():
    print('bacon')
