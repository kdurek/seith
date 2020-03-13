# imports
import player

import puzzles.numberguess


#functions
def run_game_save_score(game):
    if game == 'numberguess':
        result = puzzles.numberguess.main_loop()
        player.my_player.score[game] = result


def main_loop():
    my_player = player.create_player()
    print(my_player.name)
    

# execute
# main_loop()

run_game_save_score('numberguess')
# my_player.score['numberguess'] = puzzles.numberguess.main_loop(my_player.name)
# print(my_player.score['numberguess'])