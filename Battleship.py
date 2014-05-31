#!/usr/bin/python
__author__ = 'tal'
grid_size = 12  # Max 26 (size of the english alphabet)

from BatLib import *
import signal

#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#The 2 grids we'll be printing to the screen
if grid_size < 12:
    print draw_grid(2, grid_size, draw_rem_ships_table=False)
else:
    print draw_grid(2, grid_size)


#while True:
#print_ships(Player_Ships)
#raw_input("\nWhich one would you like to place on the grid next? Enter it's ID> ")
#    break