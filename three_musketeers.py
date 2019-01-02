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
import re

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
    # create temporary list variables in order to use the index function
    alpha = ['A', 'B', 'C', 'D', 'E']
    nums = ['1', '2', '3', '4', '5']

    try:
        if len(s) != 2:
            raise ValueError('Input value is not of length 2. Please try again.')
        elif s[0] not in alpha or s[1] not in nums:
            raise ValueError
        else:
            # return a tuple of indexes with correct location determined by matching the elements of lists alpha or num
            return (alpha.index(s[0]), nums.index(s[1]))

    except ValueError:
        print("The input value is outside of the correct range, please try again.")
        raise

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """

    # create temporary list variables in order to use the index function
    alpha = ['A', 'B', 'C', 'D', 'E']
    nums = ['1', '2', '3', '4', '5']

    try:
        if len(location) != 2:
            raise ValueError('Input value is not of length 2. Please try again.')
        elif location[0] not in range(0, 5) or location[1] not in range(0, 5):
            raise ValueError
        else:
            # return a string with correct characters determined by the matching the indexes of alpha or num
            return str(alpha[location[0]]) + str(nums[location[1]])

    except ValueError:
        print("The input value is outside of the correct range, please try again.")
        raise

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""

    # return a nested list comprehension which creates the list of all 25 possible locations
    return [(i,j) for i in range(0, 5) for j in range(0,5)]

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""

    # return modified location tuple depending on direction argument

    if direction == 'up':
        return location[0] - 1, location[1]
    elif direction == 'left':
        return location[0], location[1] - 1
    elif direction == 'down':
        return location[0] + 1, location[1]
    elif direction == 'right':
        return location[0], location[1] + 1


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

    # loop through all possible directions to check if a legal move is available, return False if not.

    can_move = False

    for direction in ['left', 'right', 'up', 'down']:
        if is_legal_move(location, direction) == True:
            can_move = True
            return can_move

    return can_move


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""

    # check for legal moves in all locations occupied by the player, return False if none are found.

    has_move = False

    for location in all_locations():
        if at(location) == who and can_move_piece_at(location) == True:
            has_move = True
            return has_move

    return has_move



def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""

    pos_moves = []

    if at(location) == '-':
        return pos_moves
    else:
        # iterates through possible directions to check if legal move exists, if so appends to possible moves list.
        for direction in ['left', 'right', 'up', 'down']:
            if is_legal_move(location, direction) == True:
                pos_moves.append(direction)

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

    # checks if adjacent location is a legal location on the board AND
    # checks if the absolute change in values is equal to 1 - this prevents illegal movement from board edges

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

    # checks each location for player, then loops through the possible moves appending them to the moves list.

    moves = []

    for location in all_locations():
        if at(location) == player:
            for i in range(len(possible_moves_from(location))):
                moves.append((location, possible_moves_from(location)[i]))

    return moves


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""

    # sets adjacent location equal to the contents of the given locations i.e. the player piece

    board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = at(location)

    # sets the given location, i.e. where the player moved from, equal to empty space '-'

    board[location[0]][location[1]] = '-'


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""

    # returns the first item in the list of possible moves for a player, i.e. "no strategy, only legality!"

    return all_possible_moves_for(who)[0]

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""

    # creates a list of current Musketeer locations

    musk_loc = []

    for location in all_locations():
        if at(location) == 'M':
            musk_loc.append(location)

    # checks if Musketeers are in the same column or the same row, if so return True (enemy wins), if not return False.

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

def get_users_move(users_side):
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}

    # added option to open a game menu instead of continuing with the current game

    move = input("Type \"menu\" for more options or continue the current game below \nEnter your next move: ").upper().replace(' ', '')

    if move.lower().replace(' ', '') == 'menu':
        open_menu(users_side)

    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move(users_side)

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move(users_side)
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
        (location, direction) = get_users_move(users_side)
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

def load_game(game_id):
    create_board()

    squares = []

    with open("gamestates.txt", "r") as file:
        data = file.readlines()

        # parse the list "data" to find the line with the matching game_id

        for i in range(1, len(data)):
            if data[i][0] == 'S':
                if data[i].split()[3] == game_id:

                    # set playing_as to the correct playing_as symbol in the line, uses regex

                    playing_as = re.findall(r':..[MR-]', data[i])

                    # loops over the next 5 lines (boardstate) and appends each square to the list "squares"

                    for j in range(i + 1, i + 6):
                        for char in list(data[j]):
                            if char == "R" or char == "M" or char == "-":
                                squares.append(char)

    # uses a list comprehension to construct a 5 x 5 matrix (board) from the squares list

    loaded_board = [squares[i:i+5] for i in range(0, 25, 5)]

    # sets loaded_board to current global game board and returns the playing_as variable

    set_board(loaded_board)

    return str(playing_as[0][-1])

def list_saved_games():
    with open("gamestates.txt", "r") as file:
        data = file.readlines()

    # loops over all lines in gamestates file, prints lines with game data i.e. beginning with "S" or "Saved"

        for line in data:
            if line[0] == 'S':
                print(line)
                print("---------------------------------------------------------")

def save_game(label, users_side):
    with open("gamestates.txt", "r") as file:
        data = file.readlines()

    # read and update the number of saved games recorded on the first line of the gamestates file

        saved_games = int(data[0].split()[4]) + 1
        data[0] = "Number of Saved Games: {}".format(saved_games) + "\n"

    with open("gamestates.txt", "w") as file:
        file.writelines(data)

    # amend gamestates file (next empty line) with new game data: label, user_side, time and boardstate

    with open("gamestates.txt", "a") as file:
        file.write("Saved Game ID: " + str(saved_games) + " " + "Saved game label: " + label + " " + "Playing as: " + " " + users_side + " " + "Game saved at: " + " " +
             str(datetime.datetime.now().replace(microsecond=0)) + "\n")
        file.writelines([str(i) + "\n" for i in get_board()])
        file.writelines("---------------------------------------------------------" + "\n")

def start_loaded_game():

    # list saved games and prompt user to choose one, then begin game from the chosen gamestate

    list_saved_games()
    game_id = input("Please type in the ID of the game you want to load: ")
    users_side = load_game(game_id)
    begin_game(users_side)

def start_new_game():

    # reset the global board, prompt user to choose a side, and begin new game

    create_board()
    users_side = choose_users_side()
    print_instructions()
    begin_game(users_side)

def open_menu(users_side):

    print("""
    +++++ You Are Playing The Three Musketeers! +++++\n
    --------------------GAME MENU--------------------\n
    **** Type \"save\" to save your current game ****\n
    **** Type \"load\" to load a previous game   ****\n
    **** Type \"new\" to start a new game        ****\n
    **** Type \"exit\" to exit the game          ****\n
    **** Type anything else to continue!       ****\n
    """)

    choice = input("Please choose an option: ").lower().replace(" ", "")

    # based on chosen option execute existing game function i.e. save_game, start_loaded_game or start_new_game

    if choice == "save":

        # passes label and user_side to the save_game function then asks user to choose a saved game to play

        label = input("Please name your saved game, for example \"nathangame1\": ")
        save_game(label, users_side)
        print("""Now choose the saved game you want to play.\n
        The game with the most recent timestamp is the one you just saved.""")
        start_loaded_game()
    elif choice == "load":
        start_loaded_game()
    elif choice == "new":
        start_new_game()
    elif choice == "exit":

        # confirms if the users wants to quit, if so uses the Python quit() function

        answer = input("Are you sure (yes/no)? ")
        if answer == "yes" or "y":
            print("Thank you for playing!")
            quit()
    else:
        print("Continuing current game...")


def start():
    """Plays the Three Musketeers Game."""

    # checks if the gamestate file exists, if not creates it

    if not os.path.exists("gamestates.txt"):
        gs = open("gamestates.txt", "w")
        gs.write("Number of Saved Games: 0" + "\n")
        gs.close()

    print("""-------------------------- Welcome to the Three Musketeers Game! --------------------------
                                      _..._
                                          ,--. /.---.\\
                                     .---/____\|--.  `
                                    (    '----'    )
                                     `-..........-'
                                       __|`--(__
                                      /'~~~/\~~'\\
                                     /   _/| )   \\
                                    /      /\     \\
                                  _/      |  |     \\
                                _/        /  \      \\
                              _///)\     (    )      )
                             / )/   )    )><><|      (
                             L/(_,  /    / ,  `\      )
                              /    /    ( / | \ )    /
                             /(    (    )_._._._(    |
                            /  )    \  /  /  \   \   |
                           /  (      \(   |  |   |\  |
                          /    )     _|__/    \__|_) |
                         /     \__   \   /    \   /( |
                        /         `. |_ /      \ _| )|
                       /            \|- |      | -| |(
                      /            ,--. |      | ,--.\\\\
                     /          gnv|____\`'==--/____|-`
    """)

    # prompts the user to choose to start a new game or load a saved game, uses the right function to start the game

    choice = input("Type \"new\" if you want to start a new game, or \"load\" if you want to load a previous game? ").lower().replace(" ", "")
    if choice == "load":
        print_instructions()
        start_loaded_game()
    else:
        start_new_game()


def begin_game(users_side):

    # starts game by printing the board state and player identity, then initiating the gameplay while loop

    print_board()
    print("You are playing as: {}".format(users_side))
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
        else:
            print("The Musketeers win!")
            break