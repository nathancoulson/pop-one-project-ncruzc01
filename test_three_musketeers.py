import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]


board2 =  [ [_, R, _, M, _],
            [_, _, R, _, _],
            [R, _, M, R, _],
            [_, R, R, _, R],
            [R, _, M, R, _] ]

board3 =  [ [M, R, _, R, _],
            [M, R, R, _, R],
            [R, _, R, R, _],
            [_, R, R, R, R],
            [R, M, _, R, _] ]

board4 =  [ [M, R, _, R, _],
            [M, R, R, _, R],
            [M, _, R, R, _],
            [_, R, R, R, R],
            [R, _, _, R, _] ]

board5 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, M, _],
            [_, _, _, R, M],
            [R, _, _, M, _] ]

board6 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, M],
            [_, _, _, M, R],
            [_, _, _, _, M] ]

board7 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, M, _],
            [_, _, _, _, M],
            [R, _, _, M, _] ]

board8 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, M, _],
            [_, _, _, M, R],
            [R, _, _, M, _] ]




def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    assert at((4, 0)) == M
    assert at((2, 1)) == R
    assert at((3, 2)) == R

def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M

    set_board(board2)
    assert at((0, 1)) == R
    assert at((3, 2)) == R
    assert at((4, 2)) == M

    set_board(board5)
    assert at((2, 3)) == M
    assert at((2, 2)) == _
    assert at((4, 0)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()

    set_board(board3)
    assert board3 == get_board()

    set_board(board4)
    assert board4 == get_board()
    assert len(board4) == 5
    assert len(board4[0]) == 5

def test_string_to_location():
    set_board(board1)
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('A9')
    assert string_to_location('A1') == (0, 0)
    assert string_to_location('B3') == (1, 2)
    assert string_to_location('E2') == (4, 1)
    assert string_to_location('D4') == (3, 3)

    set_board(board2)
    with pytest.raises(ValueError):
        string_to_location('X3T6')
    with pytest.raises(ValueError):
        string_to_location('U8')
    assert string_to_location('C3') == (2, 2)
    assert string_to_location('A5') == (0, 4)
    assert string_to_location('E1') == (4, 0)
    assert string_to_location('D2') == (3, 1)

def test_location_to_string():
    set_board(board1)
    with pytest.raises(ValueError):
        location_to_string((8,3))
    with pytest.raises(ValueError):
        location_to_string(('A', 'B'))
    assert location_to_string((1, 1)) == 'B2'
    assert location_to_string((0, 0)) == 'A1'
    assert location_to_string((4, 1)) == 'E2'
    assert location_to_string((3, 3)) == 'D4'
    assert location_to_string((1, 2)) == 'B3'

    set_board(board4)
    with pytest.raises(ValueError):
        location_to_string((2,3,4))
    with pytest.raises(ValueError):
        location_to_string(('Z', 1))
    assert location_to_string((3, 4)) == 'D5'
    assert location_to_string((0, 2)) == 'A3'
    assert location_to_string((2, 0)) == 'C1'
    assert location_to_string((4, 4)) == 'E5'
    assert location_to_string((1, 3)) == 'B4'

def test_at():
    set_board(board1)
    assert at((0, 3)) == 'M'
    assert at((1, 2)) == 'R'
    assert at((1, 3)) == 'M'
    assert at((2, 1)) == 'R'
    assert at((2, 2)) == 'M'
    assert at((4, 3)) == 'R'

def test_all_locations():
    set_board(board1)
    assert len(all_locations()) == 25
    assert all_locations()[0] == (0, 0)
    assert all_locations()[2][1] == 2
    assert all_locations()[4][0] == 0
    assert all_locations()[5] == (1, 0)

    set_board(board6)
    assert len(all_locations()) == 25
    assert all_locations()[24] == (4, 4)
    assert all_locations()[6][0] == 1
    assert all_locations()[19][1] == 4
    assert all_locations()[19] == (3, 4)

def test_adjacent_location():
    set_board(board1)
    assert adjacent_location((0, 0), "right") == (0, 1)
    assert adjacent_location((2, 4), "left") == (2, 3)
    assert adjacent_location((1, 4), "down") == (2, 4)
    assert adjacent_location((2, 2), "right") == (2, 3)
    assert adjacent_location((3, 2), "up") == (2, 2)

    set_board(board5)
    assert adjacent_location((4, 4), "left") == (4, 3)
    assert adjacent_location((5, 6), "down") == (6, 6)
    assert adjacent_location((10, 10), "up") == (9, 10)
    assert adjacent_location((1, 2), "right") == (1, 3)
    assert adjacent_location((3, 3), "left") == (3, 2)

    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((1, 2), "up")
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((4, 3), "left")
    assert is_legal_move_by_musketeer((1, 3), "down") == True
    assert is_legal_move_by_musketeer((0, 3), "left") == False
    assert is_legal_move_by_musketeer((2, 2), "up") == True
    assert is_legal_move_by_musketeer((2, 2), "left") == True
    assert is_legal_move_by_musketeer((2, 2), "right") == True
    assert is_legal_move_by_musketeer((2, 2), "down") == False
    assert is_legal_move_by_musketeer((0, 3), "up") == False
    assert is_legal_move_by_musketeer((1, 3), "right") == False
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((2, 2), "left")
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((1, 3), "down")
    assert is_legal_move_by_enemy((1, 2), "up") == True
    assert is_legal_move_by_enemy((2, 1), "right") == False
    assert is_legal_move_by_enemy((4, 3), "left") == True
    assert is_legal_move_by_enemy((4, 3), "down") == False
    assert is_legal_move_by_enemy((3, 1), "down") == True
    assert is_legal_move_by_enemy((3, 1), "up") == False
    assert is_legal_move_by_enemy((2, 3), "down") == True
    assert is_legal_move_by_enemy((2, 3), "up") == False


def test_is_legal_move():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move((0, 4), "up")
    with pytest.raises(ValueError):
        is_legal_move((3, 2), "down")
    assert is_legal_move((0, 3), "right") == False
    assert is_legal_move((0, 3), "up") == False
    assert is_legal_move((1, 2), "up") == True
    assert is_legal_move((4, 3), "left") == True
    assert is_legal_move((2, 2), "up") == True
    assert is_legal_move((2, 3), "down") == True
    assert is_legal_move((2, 3), "left") == False
    assert is_legal_move((1, 3), "left") == True
    assert is_legal_move((1, 3), "right") == False
    assert is_legal_move((2, 2), "down") == False

def test_can_move_piece_at():
    set_board(board1)

    assert can_move_piece_at((2, 1)) == True
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((4, 3)) == True
    assert can_move_piece_at((1, 2)) == True

    set_board(board4)

    assert can_move_piece_at((3, 3)) == False
    assert can_move_piece_at((2, 0)) == False
    assert can_move_piece_at((1, 2)) == True
    assert can_move_piece_at((4, 0)) == True

    set_board(board6)

    assert can_move_piece_at((3, 3)) == True
    assert can_move_piece_at((3, 4)) == False


def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True

    set_board(board6)

    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False

    set_board(board7)

    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True


def test_possible_moves_from():
    set_board(board1)

    assert possible_moves_from((2, 1)) == ['left', 'up']
    assert possible_moves_from((0, 3)) == []
    assert possible_moves_from((4, 3)) == ['left', 'right', 'up']
    assert possible_moves_from((2, 2)) == ['left', 'right', 'up']
    assert possible_moves_from((3, 1)) == ['left', 'right', 'down']
    assert possible_moves_from((2, 3)) == ['right', 'down']
    assert possible_moves_from((1, 3)) == ['left', 'down']

    set_board(board4)

    assert possible_moves_from((2, 2)) == ['left']
    assert possible_moves_from((0, 0)) == ['right']
    assert possible_moves_from((3, 3)) == []
    assert possible_moves_from((0, 3)) == ['left', 'right', 'down']


def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((2, 2)) == True
    assert is_legal_location((1, 1)) == True
    assert is_legal_location((-1, 4)) == False
    assert is_legal_location((3, 7)) == False
    assert is_legal_location((4, 4)) == True

    set_board(board3)
    assert is_legal_location((0, 4)) == True
    assert is_legal_location((10, 2)) == False
    assert is_legal_location((3, -4)) == False
    assert is_legal_location((-5, -10)) == False
    assert is_legal_location((7, 11)) == False


def test_is_within_board():
    set_board(board1)
    assert is_within_board((0, 0), "right") == True
    assert is_within_board((1, 4), "right") == False
    assert is_within_board((2, 2), "up") == True
    assert is_within_board((3, 0), "left") == False
    assert is_within_board((4, 4), "down") == False
    assert is_within_board((4, 4), "right") == False
    assert is_within_board((4, 0), "left") == False
    assert is_within_board((3, 2), "up") == True

    set_board(board2)

    assert is_within_board((3, 4), "right") == False
    assert is_within_board((4, 2), "up") == True
    assert is_within_board((1, 2), "left") == True
    assert is_within_board((0, 3), "up") == False

def test_all_possible_moves_for():
    set_board(board1)
    assert all_possible_moves_for('M') == [((1, 3), 'left'), ((1, 3), 'down'), ((2, 2), 'left'), ((2, 2), 'right'), ((2, 2), 'up')]
    set_board(board3)
    assert all_possible_moves_for('M') == [((0, 0), 'right'), ((1, 0), 'right'), ((1, 0), 'down'), ((4, 1), 'left'), ((4, 1), 'up')]
    set_board(board5)
    assert all_possible_moves_for('M') == [((2, 3), 'down'), ((3, 4), 'left'), ((4, 3), 'up')]
    set_board(board6)
    assert all_possible_moves_for('R') == []
    set_board(board7)
    assert all_possible_moves_for('R') == [((4, 0), 'right'), ((4, 0), 'up')]

def test_make_move():
    set_board(board1)
    assert make_move((2, 2), 'left') == None
    assert get_board()[2][1] == 'M'

    assert make_move((3, 1), 'down') == None
    assert get_board()[4][1] == 'R'

    assert make_move((1, 3), 'right') == None
    assert get_board()[1][4] == 'M'

    set_board(board2)
    assert make_move((1, 2), 'left') == None
    assert get_board()[1][1] == 'R'

    assert make_move((3, 4), 'down') == None
    assert get_board()[4][4] == 'R'

    assert make_move((4, 2), 'right') == None
    assert get_board()[4][3] == 'M'


def test_choose_computer_move():
    set_board(board1)
    assert choose_computer_move('R') == ((1, 2), 'left')
    set_board(board2)
    assert choose_computer_move('R') == ((0, 1), 'left')
    set_board(board3)
    assert choose_computer_move('M') == ((0, 0), 'right')
    set_board(board4)
    assert choose_computer_move('R') == ((0, 1), 'right')
    set_board(board5)
    assert choose_computer_move('M') == ((2, 3), 'down')


def test_is_enemy_win():
    set_board(board1)
    assert is_enemy_win() == False

    set_board(board2)

    assert is_enemy_win() == False

    set_board(board3)

    assert is_enemy_win() == False

    set_board(board4)

    assert is_enemy_win() == True

    set_board(board8)

    assert is_enemy_win() == True






