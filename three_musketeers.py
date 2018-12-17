# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

import os
import datetime

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

    return board

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    alpha = ['A', 'B', 'C', 'D', 'E'] #create temporary list variables in order to use the index function
    nums = ['1', '2', '3', '4', '5']

    try:
        if len(s) != 2:
            raise ValueError('Input value is not of length 2. Please try again.')
        elif s[0] not in alpha:
            raise ValueError
        elif s[1] not in nums:
            raise ValueError
        else:
            return (alpha.index(s[0]), nums.index(s[1])) #return a tuple with correct location determined by finding the index of the temporary range variables alpha or num

    except ValueError:
        print("The input value is outside of the correct range, please try again.")
        raise

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """

    alpha = ['A', 'B', 'C', 'D', 'E'] #create temporary list variables in order to use the index function
    nums = ['1', '2', '3', '4', '5']

    try:
        if len(location) != 2:
            raise ValueError('Input value is not of length 2. Please try again.')
        elif location[0] not in range(0, 5) or location[1] not in range(0, 5):
            raise ValueError
        else:
            return str(alpha[location[0]]) + str(nums[location[1]]) #return a string with correct characters determined by using the location intergers as the index of the temporary range variables alpha or num

    except ValueError:
        print("The input value is outside of the correct range, please try again.")
        raise

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    return [(i,j) for i in range(0, 5) for j in range(0,5)] #return a nested list comprehension which creates the list of all 25 possible locations

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""

    if direction == 'up':
        return location[0] - 1, location[1]
    elif direction == 'left':
        return location[0], location[1] - 1
    elif direction == 'down':
        return location[0] + 1, location[1]
    elif direction == 'right':
        return location[0], location[1] + 1

    #return modified location tuple depending on direction


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    try:
        if at(location) != 'M': #check if location contains a Musketeer 'M'
            raise ValueError("Musketeer not at given location, choose another location")
        elif is_within_board(location, direction) == False: #check if the move is legal on a 5x5 board
            return False
        elif at(adjacent_location(location, direction)) == 'R': #check if the suggested move points to a location which contains an enemy 'R'
            return True
        else:
            return False
    except ValueError:
        print("The input values are not appropriate, please try again")
        raise


def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    try:
        if at(location) != 'R': #check if location contains an enemy 'R'
            raise ValueError("Enemy not at given location, choose another location")
        elif is_within_board(location, direction) == False: #check if the move is legal on a 5x5 board
            return False
        elif at(adjacent_location(location, direction)) == '-': #check if the suggested move points to a location which contains an empty space '-'
            return True
        else:
            return False
    except ValueError:
        print("The input values are not appropriate, please try again")
        raise

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""

    try:
        if at(location) == '-':  #check if location contains an empty space '-'
            raise ValueError("Player not at given location, please select either 'M' or 'R' space")
        elif at(location) == 'M':
            return is_legal_move_by_musketeer(location, direction) #check if move is legal for Musketeer
        elif at(location) == 'R':
            return is_legal_move_by_enemy(location, direction) #check if move is legal for Enemy

    except ValueError:
        print("The input values are not appropriate, please try again")
        raise



def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""

    directions = ['left', 'right', 'up', 'down'] #define list of possible directions

    can_move = False

    for direction in directions:
        if is_legal_move(location, direction) == True:  # check if a move is legal in all directions
            can_move = True
            return can_move

    return can_move


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""

    has_move = False

    for location in all_locations():
        if at(location) == who and can_move_piece_at(location) == True: #check for legal moves in all locations occupied by the player
            has_move = True

    return has_move



def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    pos_moves = []

    directions = ['left', 'right', 'up', 'down']  # define list of possible directions

    if at(location) == '-':
        return pos_moves
    else:
        for direction in directions:
            if is_legal_move(location, direction) == True:
                pos_moves.append(direction) #iterates through possible directions and tests if they constitute a legal move, if so append to possible moves list.
    return pos_moves


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will be a pair of integer numbers."""
    if location in all_locations():
        return True
    else:
        return False
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    if ((is_legal_location(adjacent_location(location, direction)) == True) and
        (abs(adjacent_location(location, direction)[0] - location[0] <= 1)) and
            (abs(adjacent_location(location, direction)[1] - location[1] <= 1))):
        return True
    else:
        return False

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    moves = []

    if has_some_legal_move_somewhere(player) == False:
        return moves
    else:
        for location in all_locations():
            if at(location) == player:
                for i in range(len(possible_moves_from(location))):
                    moves.append((location, possible_moves_from(location)[i]))

    return moves



def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = at(location)
    board[location[0]][location[1]] = '-'


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    return all_possible_moves_for(who)[0]

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    musk_loc = []

    for location in all_locations():
        if at(location) == 'M':
            musk_loc.append(location)

    if ((musk_loc[0][0] == musk_loc[1][0] and musk_loc[1][0] == musk_loc[2][0]) or
        (musk_loc[0][1] == musk_loc[1][1] and musk_loc[1][1] == musk_loc[2][1])):
        return True
    else:
        return False

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def load_game(label):
    board = create_board()

def save_game(label, users_side):
    with open("gamestates.txt", "r") as file:
        data = file.readlines()

        saved_games = int(data[0].split()[4]) + 1

        data[0] = "Number of Saved Games: {}".format(saved_games) + "\n"

    with open("gamestates.txt", "w") as file:
        file.writelines(data)

    with open("gamestates.txt", "a") as file:
        file.write("Saved Game ID: " + str(saved_games) + " " + "Saved game label: " + label + " " + "Playing as: " + " " + users_side + " " + "Game saved at: " + " " +
             str(datetime.datetime.now().replace(microsecond=0)) + "\n")
        file.writelines([str(i) + "\n" for i in get_board()])
        file.writelines("---------------------------------------------------------" + "\n")


def start():
    """Plays the Three Musketeers Game."""

    #check if the gamestate file exists, if not create it.
    if not os.path.exists("gamestates.txt"):
        gs = open("gamestates.txt", "w")
        gs.write("Number of Saved Games: 0" + "\n")
        gs.close()

    print("Welcome to the Three Musketeers Game!")
    print("Type \"new\" if you want to start a new game, or \"load\" if you want to load a previous game?", end="")
    choice = input()
    if choice == "load":
        print("Please type in the name of your saved game: ", end="")
        board = load_game(input())
    else:
        create_board()

    users_side = choose_users_side()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):

            move_musketeer(users_side)

            print_board()

            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            move_enemy(users_side)
            print_board()

            answer = input("Do you want to save your game at this point? (answer yes or no): ")
            if answer == "yes" or answer == "y":
                label = input("Please name your saved game, for example \"nathangame1\": ")
                save_game(label, users_side)

        else:
            print("The Musketeers win!")
            break

start()