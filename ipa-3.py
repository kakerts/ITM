'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
    #check if to_member is followed by from_member and if from_member is followed by to_member
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
    #checks if from_member is followed by to_member
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
    #check if to_member is followed by from_member
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)

    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
        #checks if all elements in the row are the same and not empty. if it is, that symbol is returned

    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if len(set(column)) == 1 and column[0] != '':
            return column[0]
        #extracts each column and checks if all elements in column are same and not empty. if so, that symbol is returned

    diagonal1 = [board[i][i] for i in range(size)]
    diagonal2 = [board[i][size - i - 1] for i in range(size)]
    if len(set(diagonal1)) == 1 and diagonal1[0] != '':
        return diagonal1[0]
    if len(set(diagonal2)) == 1 and diagonal2[0] != '':
        return diagonal2[0]
    #create two lists representing diagonal1 (top-left to bottom-right) and diagonal2 (top-right to bottom-left).
    #checks if all elements in each diagonal are the same and not empty. if so, that symbol is returned


    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
    #loop continues until current_stop is equal to second_stop, (shuttle has arrived at the destination/second stop)
        current_leg = route_map[current_stop]
        #retrieves current_leg from the route_map.
        total_time += current_leg['travel_time_mins']
        #adds the travel time of the current leg to total_time
        current_stop = current_leg['next_stop']
        #updates the current_stop with the next stop from the current leg and loop continues until destination is reached
    return total_time