# imports
import platform
import os
import sys

import random

# functions


def greet_user(attempts):
    print('\nWylosowałem dla Ciebie słowo.\n'
          'Twoim zadaniem będzie typowanie literek.\n'
          'Jeśli słowo będzie zawierać Twój typ,\n'
          'zostanie odpowiednio oznaczone, do dzieła!')


def roll_word():
    words = ['kot', 'czarownica']
    return list(random.choice(words))


def guess_char():
    while True:
        guess = input('\nWytypuj literę: ')

        if guess.isalpha():
            return guess.lower()
        else:
            print('\nDozwolone są tylko litery!')


def find_indexes(guess, word):
    indexes = []
    for idx, char in enumerate(word):
        if guess == char:
            indexes.append(idx)

    return indexes


def fill_indexes(guess, word, indexes):
    for idx in indexes:
        word[idx] = guess


def print_space():
    print('_' * 60)
    print()


def try_again():
    print('Czy chcesz spróbować jeszcze raz?')
    while True:
        again = input('> ')
        if again in ['y', 't', 'yes', 'tak']:
            if platform.system() == 'Windows':
                os.system('cls')
                break
            else:
                os.system('clear')
                break
        elif again in ['n', 'no', 'nie']:
            print('\nDziękuję za gre!')
            sys.exit()
        else:
            print('\nNiepoprawny wybór!')


# main loop
def main_loop():
    while True:
        attempts = 3
        random_word = roll_word()
        guess_word = ['_' for char in random_word]

        greet_user(attempts)
        print_space()
        while True:
            if attempts == 0:
                print_space()
                print('Przegrałeś!')
                print()
                break

            print(guess_word)
            print(f'\nPozostało prób: {attempts}')
            guess = guess_char()

            if guess == ''.join(random_word):
                print_space()
                print('Wygrałeś!')
                print()
                break

            if len(guess) > 1:
                print_space()
                print('Możesz typować tylko jedną literke na raz!')
                print()
                continue

            if guess in random_word:
                indexes = find_indexes(guess, random_word)
                fill_indexes(guess, guess_word, indexes)
                print_space()
                print('Brawo trafione!')
                print()
            else:
                print_space()
                print('Niestety, pudło!')
                print()
                attempts -= 1

            if '_' not in guess_word:
                print_space()
                print('Wygrałeś!')
                print()
                break

        try_again()
    return attempts


# execute
