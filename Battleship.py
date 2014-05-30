#!/usr/bin/python
__author__ = 'tal'
grid_size = 16  # Max 26 (size of the english alphabet)

from BatLib import *
import signal

#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#The 2 grids we'll be printing to the screen
print draw_grid(2, grid_size)

#while True:
    #print_ships(Player_Ships)
    #raw_input("\nWhich one would you like to place on the grid next? Enter it's ID> ")
#    break