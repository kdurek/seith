# imports
import pickle


class Player:
    def __init__(self):
        self.name = None
        self.score = {'numberguess': 3}

# functions


def save(variable):
    with open('save_player.pkl', 'wb') as data:
        pickle.dump(variable, data, pickle.HIGHEST_PROTOCOL)


def load():
    with open('save_player.pkl', 'rb') as data:
        global my_player
        my_player = pickle.load(data)


def init_player():
    try:
        with open('save_player.pkl', 'rb') as data:
            return pickle.load(data)

    except IOError:
        my_player = Player()
        print('Cześć! Jak masz na imię?')
        my_player.name = input('> ').capitalize()
        save(my_player)
        return my_player


# execute
my_player = init_player()
