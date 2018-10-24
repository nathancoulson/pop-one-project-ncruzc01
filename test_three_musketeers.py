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

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A0') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    assert location_to_string((1,1)) == '1,1'

def test_at():
    assert at((1,1)) == '_'

def test_all_locations():
    assert all_locations() == [(0,0),(1,2)]

def test_adjacent_location():
    assert adjacent_location((0,0),"right") == (0,1)
    
def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((1,3), "down") == True
    
def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((1,2), "up") == True

def test_is_legal_move():
    assert is_legal_move((0,3),"right") == True

def test_can_move_piece_at():
    assert can_move_piece_at((2,1)) == True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert possible_moves_from((2,1)) == ['left', 'up']

def test_is_legal_location():
    assert is_legal_location((2,2)) == True

def test_is_within_board():
    assert is_within_board((0,0), "right") == True

def test_all_possible_moves_for():
    assert all_possible_moves_for('M') == [((0,1), 'right'),((0,2), 'left')]
    
def test_make_move():
    assert make_move() == 0
    
def test_choose_computer_move():
    assert choose_computer_move('R') == ((2,2), 'down') #should work for both 'M' and 'R'

def test_is_enemy_win():
    assert is_enemy_win() == True

#commentary

