#!/usr/bin/env python3

import random


def get_dice_sides():
    while True:
        try:
            return int(input('How many sides is your dice? '))
        except ValueError:
            print('Please enter a number.')


if __name__ == '__main__':
    n_sides = get_dice_sides()
    while True:
        typed = input('Roll the dice ("y" to roll, "quit" to quit)? ').lower()
        if typed == 'quit':
            print('Thank you for playing, enjoy your day! :)')
            break
        elif typed in ('y', 'yes', 'roll'):
            print(f'You rolled a {random.randint(1, n_sides)}!')
