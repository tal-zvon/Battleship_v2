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

    #Draw graph labels
    if num_of_grids == 1:
        print ' ' * 10 + "Player"
        print

        #Draw top labels on graph
        print ' ' * 2,
        for i in range(1, grid_size + 1):
            print i,
        print

        #Draw row of underscores
        print ' ' * 3 + '-' * ((grid_size * 2) - 1)

        #Draw one graph
        for y in range(0, grid_size):
            #Print y axis
            print 'A|',
            #Draw graph row
            for x in range(0, grid_size):
                print 'O',
            print

    elif num_of_grids == 2:
        print ' ' * 10 + "Player" + ' ' * 10 + "Computer"

        #Draw two graphs