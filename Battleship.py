#!/usr/bin/python
__author__ = 'tal'
grid_size = 19  # Max 26 (size of the english alphabet)

from BatLib import *
import signal
import os

#Declare 2 lists of remaining ships
player_ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}
computer_ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}


#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#Ask user where he wants to put the ships
while True:
    #Clear screen
    os.system('clear 2>/dev/null')

    # noinspection PyRedeclaration
    ship_being_placed = -1
    current_ship_place = []


    print draw_grid(1, grid_size, player_ships, computer_ships)
    print '\n\n'
    print print_ships(player_ships, grid_size, dynamic=False)
    answer = raw_input("\nWhich ship would you like to place on the grid next? Enter it's ID> ")
    try:
        answer = int(answer)
    except ValueError:
        print '\n"%s" is not a number!' % answer
        raw_input("Press enter to continue.")
        continue

    if not 1 <= answer <= 5:
        print '\nInvaid number! Please enter a number between 1 and 5.'
        raw_input("Press enter to continue.")
        continue

    # noinspection PyRedeclaration
    ship_being_placed = answer

    answer = raw_input("Where would you like to place it? (ex A10)> ")

    if not answer[0].isalpha():
        print '\nThe coordinates you entered are in an invalid format!'
        raw_input("Press enter to continue.")
        continue

    if not answer[1:].isdigit():
        print '\nThe coordinates you entered are in an invalid format!'
        raw_input("Press enter to continue.")
        continue

    # noinspection PyRedeclaration
    current_ship_place = [answer[0], int(answer[1:])]

    #Check if letter is within range
    if not ord('a') <= ord(current_ship_place[0]) < (ord('a') + grid_size):
        print '\nThe coordinates you entered are out of range!'
        raw_input("Press enter to continue.")
        continue

    #Check if number is within range
    if current_ship_place[1] < 0 or current_ship_place[1] > grid_size:
        print '\nThe coordinates you entered are out of range!'
        raw_input("Press enter to continue.")
        continue

    #Ask for the angle of the ship (up, down, left, right)


#The 2 grids we'll be printing to the screen
'''
if grid_size < 12:
    print draw_grid(2, grid_size, draw_rem_ships_table=False)
else:
    print draw_grid(2, grid_size)
    print print_ships(player_ships, grid_size, dynamic=False)
'''