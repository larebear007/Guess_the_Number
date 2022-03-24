# GUESS THE NUMBER

import random

print('Hello! Welcome to Guess the Number')


def r_100():
    turn = 0
    secret_num = random.randint(1, 100)
    while True:
        try:
            print('Let\'s get started . . .\n')
            x = input('Pick a number between 1 and 100: ')
            x = int(x)
            turn += 1
            if x == secret_num:
                break
            elif x > secret_num:
                print('Your guess', x, 'is too high.')
                continue
            elif x < secret_num:
                print('Your guess', x, 'is too low.')
                continue
        except:
            print('Please use your number pad to enter a number.')

    print('\nYou got it! The magic number was', secret_num)
    print('It took you', turn, 'turns to win.')


def r_neg100():
    turn = 0
    secret_num = random.randint(-100, 100)
    while True:
        try:
            print('Let\'s get started . . .\n')
            x = input('Pick a number between 1 and 100: ')
            x = int(x)
            turn += 1
            if x == secret_num:
                break
            elif x > secret_num:
                print('Your guess', x, 'is too high.')
                continue
            elif x < secret_num:
                print('Your guess', x, 'is too low.')
                continue
        except:
            print('Please use your number pad to enter a number.')

    print('\nYou got it! The magic number was', secret_num)
    print('It took you', turn, 'turns to win.')

