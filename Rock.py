'''
Rock Paper Scissors
'''

import random
import os 
import re

def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again?(Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

    def play_rps():
        play = True
        while play:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('')
            print('Rock, Paper, Scissors - Shoot!')

            user_choice = input('Choose your weapon'
                                '[R]ock], [P]aper, or [S]cissors: ')
            if not re.match("[SsRrPp]", user_choice):
                print('Please choose a letter: ')
                print('Rock], [P]aper, or [S]cissors')
                continue
        