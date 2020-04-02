# imports
import os
import sys

import player
from player import my_player

from puzzles import numberguess, hangman


# functions
def main_menu():
    while True:
        print('Co chcesz zrobić?\n'
              '[1] Statystyki\n'
              '[2] Wybór gry\n'
              '[Q] Wyjdź')
        choice = input('> ')

        if choice.lower().startswith('q'):
            print('\nDo zobaczenia!')
            break

        try:
            choice = int(choice)
            if choice not in [1, 2, 3]:
                continue
        except ValueError:
            continue

        print()

        if choice == 1:
            show_stats()
        elif choice == 2:
            game_launcher()


def show_stats():
    print(f'Statystyki gracza {my_player.name}')
    print()
    for game, score in my_player.score.items():
        print(str(game) + ': ' + str(score))

    print('[Q] Wstecz')
    while True:
        choice = input('> ')

        if choice.lower().startswith('q'):
            break
    print()


def game_launcher():
    while True:
        print('Którą grę wybierasz?\n'
              '[1] Zgadnij liczbę\n'
              '[2] Wisielec\n'
              '[Q] Wstecz')
        choice = input('> ')

        if choice.lower().startswith('q'):
            break

        try:
            choice = int(choice)
            if choice not in [1, 2, 3]:
                continue
        except ValueError:
            continue

        if choice == 1:
            my_player.score['numberguess'] = numberguess.main_loop()
        elif choice == 2:
            my_player.score['hangman'] = hangman.main_loop()
        print()

# execute


def main_loop():
    player.init_player()
    player.save(my_player)
    # main_menu()
    show_stats()

# execute


main_loop()

# player.score['numberguess'] = puzzles.numberguess.main_loop(player.name)
# print(player.score['numberguess'])
