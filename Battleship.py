#!/usr/bin/python
__author__ = 'tal'
grid_size = 19  # Max 26 (size of the english alphabet)

from BatLib import *
import signal

#Declare 2 lists of remaining ships
player_ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}
computer_ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}


#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#Ask user where he wants to put the ships
while True:
    print draw_grid(1, grid_size, player_ships, computer_ships)
    print '\n\n'
    print print_ships(player_ships, grid_size, dynamic=False)
    raw_input("\nWhich one would you like to place on the grid next? Enter it's ID> ")
    break

#The 2 grids we'll be printing to the screen
'''
if grid_size < 12:
    print draw_grid(2, grid_size, draw_rem_ships_table=False)
else:
    print draw_grid(2, grid_size)
'''