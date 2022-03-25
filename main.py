# GUESS THE NUMBER

import random
import time


def level1():
    red = "\033[0;31m"
    blue = "\033[0;34m"
    end = "\033[0;0m"

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

    print('\nYOU GOT IT! The magic number was', blue + str(secret_num) + end)
    print('It took you', turn, 'turns to win.')


def level3():
    red = "\033[0;31m"
    blue = "\033[0;34m"
    end = "\033[0;0m"

    print('Let\'s get started . . .\n')
    turn = 0
    secret_num = random.randint(1, 100)
    while True:
        try:
            if turn == 6:
                print('You have 1 turn left . . .')
            if turn == 7:
                print(red + 'Ah rats! You are all out of turns.' + end)
                print('The secret number was', secret_num)
                break
            x = input('Pick a number between 1 and 100: ')
            x = int(x)

            turn += 1
            if x == secret_num:
                print('\nYOU GOT IT! The magic number was', blue + str(secret_num) + end)
                print('It took you', turn, 'turns to win.')
                break
            elif x > secret_num:
                print('Your guess', x, 'is too high.')
                continue
            elif x < secret_num:
                print('Your guess', x, 'is too low.')
                continue
        except:
            print('Please use your number pad to enter a number.')


def level2():
    red = "\033[0;31m"
    blue = "\033[0;34m"
    end = "\033[0;0m"

    turn = 0
    secret_num = random.randint(-100, 100)
    while True:
        try:
            print('Let\'s get started . . .\n')
            x = input('Pick a number between -100 and 100: ')
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

    print('\nYOU GOT IT! The magic number was', blue + str(secret_num) + end)
    print('It took you', turn, 'turns to win.')


def level4():
    red = "\033[0;31m"
    blue = "\033[0;34m"
    end = "\033[0;0m"

    print('Let\'s get started . . .\n')
    turn = 0
    secret_num = random.randint(-100, 100)
    while True:
        try:
            if turn == 8:
                print('You have 1 turn left . . .')
            if turn == 9:
                print(red + 'Ah rats! You are all out of turns.' + end)
                print('The secret number was', blue + str(secret_num) + end)
                break
            x = input('Pick a number between -100 and 100: ')
            x = int(x)

            turn += 1
            if x == secret_num:
                print('\nYOU GOT IT! The magic number was', blue + str(secret_num) + end)
                print('It took you', turn, 'turns to win.')
                break
            elif x > secret_num:
                print('Your guess', x, 'is too high.')
                continue
            elif x < secret_num:
                print('Your guess', x, 'is too low.')
                continue
        except:
            print('Please use your number pad to enter a number.')


while True:
    print('Hello! Welcome to Guess the Number')
    time.sleep(.8)
    print('Which level would you like to play?')
    time.sleep(.5)
    print('LEVEL 1: (Easy)     1 to 100')
    time.sleep(.5)
    print('LEVEL 2: (Easy)  -100 to 100')
    time.sleep(.5)
    print('LEVEL 3: (Hard)     1 to 100')
    time.sleep(.5)
    print('LEVEL 4: (Hard)  -100 to 100')
    time.sleep(.5)
    print('(In the hard levels you only have 6 guesses to get the number.)')
    while True:
        choice = input('\nEnter 1, 2, 3, or 4 for your choice:  ')
        if choice == '1':
            level1()
            break
        elif choice == '2':
            level2()
            break
        elif choice == '3':
            level3()
            break
        elif choice == '4':
            level4()
            break
        else:
            print('Please enter a valid option.')
            continue

    print('Thanks for playing Guess the Number!')
    restart = input('Would you like to play again (yes or no)?  ')
    if restart.lower() == 'yes' or restart.lower() == 'y':
        continue
    else:
        break

print('Come again any time :)')
quit()
