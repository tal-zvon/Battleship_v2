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


def offset_grids(str1, str2, offset, spacing):
    """
    Offsets 2 grids
    Ex1 - negative offset with some spacing:

        ***
        ***  ***
             ***

    Ex2 - positive offset with 0 spacing:

           ***
        ******
        ***

    :param str str1: The first grid
    :param str str2: The second grid
    :param int offset: The amount and direction the grids should be moved. Can be a positive or negative int.
    :param int spacing: The amount of space between the grids
    :rtype : str
    """

    #The variable that will store the combined
    #grids
    rtn_val = ''

    #Figure out the longest line in str1
    longest_line = 0
    for i in range(0, len(str1.split('\n'))):
        if len(str1.split('\n')[i]) > longest_line:
            longest_line = len(str1.split('\n')[i])

    #Loop for every line we need to print
    for i in range(0, len(str1.split('\n')) + abs(offset)):
        #If the offset is negative, move second grid down
        if offset < 0:
            #The following "if" statement check if we should only print a line from grid 1, only print a line from
            #grid 2, or both. It figures out which line should be printed for each grid (based on the offset), makes
            #sure lines are properly aligned with spaces, and that blank lines are done right
            if i < abs(offset) and i < len(str1.split('\n')):
                rtn_val += str1.split('\n')[i] + '\n'
            elif abs(offset) <= i < len(str1.split('\n')):
                rtn_val += str1.split('\n')[i] + ' ' * spacing + str2.split('\n')[i - abs(offset)] + '\n'
            elif abs(offset) <= i < abs(offset) + len(str2.split('\n')):
                rtn_val += ' ' * longest_line + ' ' * spacing + str2.split('\n')[i - abs(offset)] + '\n'
            else:
                rtn_val += '\n'
        #If the offset is positive, move second grid up
        elif offset > 0:
            #The following "if" statement check if we should only print a line from grid 1, only print a line from
            #grid 2, or both. It figures out which line should be printed for each grid (based on the offset), makes
            #sure lines are properly aligned with spaces, and that blank lines are done right
            if i < offset and i < len(str2.split('\n')):
                rtn_val += ' ' * longest_line + ' ' * spacing + str2.split('\n')[i] + '\n'
            elif offset <= i < len(str2.split('\n')):
                rtn_val += str1.split('\n')[i - offset] + ' ' * spacing + str2.split('\n')[i] + '\n'
            elif len(str2.split('\n')) <= i >= offset:
                rtn_val += str1.split('\n')[i - offset] + '\n'
            else:
                rtn_val += '\n'
        #If the offset is 0, keep grids on same line
        elif offset == 0:
            rtn_val += str1.split('\n')[i] + ' ' * spacing + str2.split('\n')[i] + '\n'
    return rtn_val


def draw_grid(num_of_grids, grid_size, grid_title='Player', draw_rem_ships_table=True):
    """
    Draw either one or two grids on the screen

    :param int num_of_grids: Number of grids to draw. Can only be 1 or 2
    :param int grid_size: The size of the grid square
    :param str grid_title: The title to write above the grid. The default is None, so the argument
        can be omitted
    :param bool draw_rem_ships_table: True if you want the remaining ships table drawn. False if you don't.
    :rtype : string
    """

    #The variable we'll be returning -
    #the actual grid we drew
    grid = ''

    #We can only draw one or two grids
    if num_of_grids < 1 or num_of_grids > 2:
        print "The number of grids can only be 1 or 2!"
        exit(1)

    #Draw grid labels
    if num_of_grids == 1:
        #Aligns the title to the middle of the grid
        grid += (' ' * 4 + ' ' * (grid_size - (len(grid_title) / 2)) + grid_title + ' ' * (grid_size -
                                                                                           (len(grid_title) / 2)))
        #On the empty line between the grid title and the
        #y axis, put spaces to keep proper alignment for an
        #offset second grid
        grid += '\n' + ' ' * (grid_size * 2 + 4) + '\n'

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
            grid += ' ' * 4
            for i2 in range(0, grid_size):
                #If grid_size is 10, don't worry about the order of
                #magnitude - just print one row
                if grid_size == 10:
                    grid += number_list[i2]
                    #Don't add a space after number 10
                    #to keep proper alignment
                    if i2 != 9:
                        grid += ' '
                else:
                    grid += number_list[i2][i] + ' '
            grid += '\n'

        #Draw row of underscores
        if grid_size != 10:
            grid += ' ' * 4 + '-' * ((grid_size * 2) - 1) + ' '
        else:
            grid += ' ' * 4 + '-' * (grid_size * 2)
        grid += '\n'

        #Draw one grid
        for y in range(0, grid_size):
            #Print y axis
            grid += '%s |' % chr(ord('a') + y).upper() + ' '
            #Draw grid row
            for x in range(0, grid_size):
                grid += 'O '
            #Don't print the final newline
            if y != grid_size - 1:
                grid += '\n'

        return grid

    elif num_of_grids == 2:
        #Create 2 grids
        first_grid = draw_grid(1, grid_size, "Player")
        second_grid = draw_grid(1, grid_size, "Computer")

        #Combine the grids
        combined_grids = offset_grids(first_grid, second_grid, -1 * (len(first_grid.split('\n')) - 2), 0)

        #If this function was called with draw_rem_ships_table set to True, draw the remaining ships table
        if draw_rem_ships_table:
            #Declare 2 lists of remaining ships
            Player_Ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}
            Computer_Ships = {'Aircraft Carrier': 1, 'Battleship': 1, 'Cruiser': 1, 'Destroyer': 2, 'Submarine': 2}

            rem_player_ships = print_ships(Player_Ships)
            rem_computer_ships = print_ships(Computer_Ships)

            combined_grids_with_rem_ships_table = ''

            #Start position
            if grid_size <= 10:
                start_pos = 2
            elif 10 < grid_size < 15:
                start_pos = 3
            else:
                start_pos = ((grid_size + 4) / 2) - (len(rem_player_ships.split('\n')) / 2)

            for LINE in range(0, len(combined_grids.split('\n'))):
                if start_pos <= LINE < start_pos + len(rem_player_ships.split('\n')):
                    combined_grids_with_rem_ships_table += combined_grids.split('\n')[LINE] + ' ' * 5 + rem_player_ships.split('\n')[LINE - start_pos] + '\n'
                else:
                    combined_grids_with_rem_ships_table += combined_grids.split('\n')[LINE] + '\n'

            return combined_grids_with_rem_ships_table
        else:
            return combined_grids


# noinspection PyUnusedLocal,PyUnusedLocal
def signal_handler(signal, frame):
    """
    Handles Ctrl+C
    """
    print "\n"
    print "You sank my battleship!"
    exit(0)


def print_ships(ships_remaining):
    """
    Prints the table of remaining ships

    :param dict ships_remaining: A dictionary of the ships remaining
    :rtype : string
    """

    #Return value - the
    rtn = ''
    #rtn += "These are your ships:\n\n"
    rtn += '  ID  |  #  |         Ship         |   Size' + '\n'
    rtn += '-' * 46 + '\n'
    rtn += '   1  | %dx  |   Aircraft Carrier   |    5    ' % ships_remaining['Aircraft Carrier'] + '\n'
    rtn += '   2  | %dx  |   Battleship         |    4    ' % ships_remaining['Battleship'] + '\n'
    rtn += '   3  | %dx  |   Cruiser            |    3    ' % ships_remaining['Cruiser'] + '\n'
    rtn += '   4  | %dx  |   Destroyer          |    2    ' % ships_remaining['Destroyer'] + '\n'
    rtn += '   5  | %dx  |   Submarine          |    1    ' % ships_remaining['Submarine']

    return rtn