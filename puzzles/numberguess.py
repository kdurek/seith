# imports
import platform
import os
import sys

cur_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(cur_path)
sys.path.append(parent_path)

import random

from .. import player


class Game:
    def __init__(self, high_num, my_name):
        self.high_num = high_num
        self.my_name = my_name
        self.guesses_taken = 0
        self.number = random.randint(1, self.high_num)
        self.guess = None

    def get_guess(self):
        print('Wytypuj liczbę:')
        try:
            self.guess = int(input('> '))
        except ValueError:
            print('Dozwolone są tylko liczby!\n')
            return False
        return True

    def play(self):
        print(f'Hej {self.my_name}!'
              f'Wylosowałem dla Ciebie liczbę z przedziału od 1 do {self.high_num}.\n'
              'Twoim zadaniem będzie odgadnąć co to za liczba, do dzieła!\n\n')
        # f'Ilość prób: {self.guesses_taken}\n')

        while self.guesses_taken < 6:
            if not self.get_guess():
                continue
            # else: self.guess gets changed in get_guess function

            self.guesses_taken += 1

            if self.guess < self.number:
                print('Za mała liczba!')

            if self.guess > self.number:
                print('Za duża liczba!')

            if self.guess == self.number:
                break

        if self.guess == self.number:
            print(f'Dobra robota, {self.my_name}! Zgadłeś moją liczbę za {self.guesses_taken} razem!')
            return self.guesses_taken
        else:
            print(f'Niestety. Liczba o której myślałem to {self.number}')

# functions
def main_loop(my_name):
    print(f"Okej, {my_name}! Mamy dwa poziomy trudności.")

    while True:
        print('Wpisz [1] dla łatwego, [2] dla normalnego lub [3] dla trudnego poziomu trudności. Wpisz [q] aby wyjść.')
        user_choice = input('> ')

        if user_choice.lower().startswith('q'):
            print('Dzięki za gre!')
            break

        try:
            user_choice = int(user_choice)
            if user_choice not in [1, 2, 3]:
                continue
        except ValueError:
            continue

        if user_choice == 1:
            easy_game = Game(20, my_name)
            game_result = easy_game.play()

        elif user_choice == 2:
            norm_game = Game(40, my_name)
            game_result = norm_game.play()
            
        elif user_choice == 3:
            hard_game = Game(60, my_name)
            game_result = hard_game.play()

        print('\nMoże kolejna?')

    return game_result

