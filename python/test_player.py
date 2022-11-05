from player import Player
import pytest

@pytest.fixture(scope="function")
def player1() -> Player:
    return Player(
        name="John",
        place=0,
    )

def test_init_player():
    assert Player(name="John", place=0)


def test_player_penalty_box(player1: Player):    
    assert player1.in_penalty_box == False 

    player1.move_in_penalty_box()
    assert player1.in_penalty_box == True

    player1.move_out_penalty_box()
    assert player1.in_penalty_box == False

def test_player_move_place(player1: Player):
    player1.move_place(count=13) # Board resets on 12th position
    assert player1.place == 1


def test_player_display_coins(player1):
    pass 
