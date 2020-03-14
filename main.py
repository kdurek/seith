# imports
import player
from player import my_player

from puzzles import numberguess, hangman


# functions
def game_launcher():

    while True:
        print('Którą grę wybierasz?\n'
              '[1] Zgadnij liczbę\n'
              '[2] Wisielec')
        choice = input('> ')

        if choice.lower().startswith('q'):
            print('\nWyjście!')
            break

        try:
            choice = int(choice)
            if choice not in [1, 2, 3]:
                continue
        except ValueError:
            continue

        print()

        if choice == 1:
            my_player.score['Numero Zgadulo'] = numberguess.main_loop(my_player.name)
        elif choice == 2:
            my_player.score['Wisielec'] = hangman.main_loop()


def main_loop():
    player.init_player()
    print(my_player.name)
    game_launcher()

# execute


main_loop()


# player.score['numberguess'] = puzzles.numberguess.main_loop(player.name)
# print(player.score['numberguess'])
