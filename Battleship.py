#!/usr/bin/python
__author__ = 'tal'
grid_size = 10  # Max 26 (size of the english alphabet)

from BatLib import *
import signal

#Declare 2 lists of remaining ships
Player_Ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}
Computer_Ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}

#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#Display grid
print draw_grid(2, grid_size)

while True:
    print_ships(Player_Ships)
    #raw_input("\nWhich one would you like to place on the grid next? Enter it's ID> ")
    break