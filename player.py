class Player:
    def __init__(self, name):
        self.name = name
        self.score = {}
        

def create_player():
    print('Cześć! Jak masz na imię?')
    my_name = input('> ').capitalize()

    return Player(my_name)