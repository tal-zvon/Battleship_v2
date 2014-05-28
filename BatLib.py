__author__ = 'tal'


class Coordinate(object):
    def __init__(self, ship_here, fired_here):
        """
        Stores the 2 things you need to know about a coordinate: Is there a ship there, and have we
            already shot there

        :param bool ship_here: True if part of a ship is at these coordinates, False otherwise
        :param bool fired_here: True if we already bombed these coordinates, False otherwise
        """

        self.ship_here = ship_here
        self.fired_here = fired_here


def draw_grid(num_of_grids, grid_size):
    """
    Draw either one or two grids on the screen

    :param int grid_size: The size of the grid square
    :param int num_of_grids: Number of grids to draw. Can only be 1 or 2
    :rtype : None
    """

    #We can only draw one or two grids
    if num_of_grids < 1 or num_of_grids > 2:
        print "The number of grids can only be 1 or 2!"
        exit(1)

    #Draw grid labels
    if num_of_grids == 1:
        #Note: The following line properly centers the grid title ("Player")
        #because the size of half the word "Player" is 3 characters - exactly
        #the same as the 3 character left border, which cancel each other out
        print ' ' * grid_size + "Player"
        print

        #The order of magnitude of the last number in the grid
        #Ex. '1' for 0-9, '2' for 10 - 99, etc.
        #Used to calculate how many vertical lines the numbers will take to print
        grid_order_of_magnitude = len(str(grid_size))

        #10 is a special case. If our grid is grid_size = 10, let it
        #hang off the side instead of printing 2 rows of numbers
        if grid_size == 10:
            grid_order_of_magnitude = 1

        #Declare a list, and fill it with numbers (as strings)
        #between 1 and the last number in the grid, with leading zeros
        number_list = []
        for i in range(1, grid_size + 1):
            if len(str(i)) < grid_order_of_magnitude:
                number_list.append("0" * (grid_order_of_magnitude - len(str(i))) + str(i))
            else:
                number_list.append(str(i))

        #Draw top labels on grid
        #For each order of magnitude, print a new vertical line
        #This just prints numbers up and down instead of sideways
        for i in range(0, grid_order_of_magnitude):
            print ' ' * 2,
            for i2 in range(0, grid_size):
                #If grid_size is 10, don't worry about the order of
                #magnitude - just print one row
                if grid_size == 10:
                    print number_list[i2],
                else:
                    print number_list[i2][i],
            print

        #Draw row of underscores
        print ' ' * 3 + '-' * ((grid_size * 2) - 1)

        #Draw one grid
        for y in range(0, grid_size):
            #Print y axis
            print '%s|' % chr(ord('a') + y).upper(),
            #Draw grid row
            for x in range(0, grid_size):
                print 'O',
            print

    elif num_of_grids == 2:
        print ' ' * 10 + "Player" + ' ' * 10 + "Computer"

        #Draw two grids