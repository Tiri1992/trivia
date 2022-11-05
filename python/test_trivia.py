from trivia import Game
from category import Category
from player import Player
from errors import NotEnoughPlayersError
import pytest

@pytest.fixture(scope="function")
def init_game_with_players() -> Game:
    players = [
        Player(name="John", place=0),
        Player(name="Alex", place=0),
    ]
    return Game(
        players=players,
    )

def test_game_create_raises():
    game = Game(
        players=[Player(name="John", place=0)]
    )
    
    with pytest.raises(NotEnoughPlayersError) as err:
        game.create()

def test_game_current_category(init_game_with_players: Game):

    # Validate correct returned categories for position of player
    game = init_game_with_players
    game.create()

    assert game._current_category == Category.POP

    game.current_player.move_place(count=1)
    assert game._current_category == Category.SCIENCE


def test_game_roll_in_penalty_box(init_game_with_players: Game):
    game = init_game_with_players
    game.create()
    assert game.current_player.name == "John"
    game.current_player.move_in_penalty_box()
    ROLL = 13
    game.roll(ROLL)

    assert game.current_player.in_penalty_box == False 


def test_game_move_into_penalty_box(init_game_with_players: Game):
    game = init_game_with_players
    game.create()

    # Odd roll that is more than 11
    ROLL = 12
    game.roll(ROLL)

    game.wrong_answer()

    assert len(game.get_players_in_penalty_box()) == 1

def test_game_next_player(init_game_with_players: Game):
    game = init_game_with_players
    
    assert game.current_player.name == "John"

    game.next_player()

    assert game.current_player.name == "Alex"