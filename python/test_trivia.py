from trivia import Game
from category import Category
import pytest

@pytest.fixture(scope="function")
def init_game() -> Game:
    return Game()

@pytest.fixture(scope="function")
def init_game_with_players() -> Game:
    game = Game()
    game.add("John")
    game.add("Alex")
    return game 

def test_game_is_playable(init_game: Game):
    # Add sufficient number of players to play
    init_game.add("John")
    
    # Should not be playable with one player
    assert init_game.is_playable() == False 
    
    # Add player
    init_game.add("Alex")

    # Now should be playable
    assert init_game.is_playable()

def test_game_current_category(init_game_with_players: Game):

    # Validate correct returned categories for position of player
    game = init_game_with_players
    

    game.places[game.current_player] = 0
    assert game._current_category == Category.POP

    game.places[game.current_player] = 4
    assert game._current_category == Category.POP

    game.places[game.current_player] = 8
    assert game._current_category == Category.POP

    game.places[game.current_player] = 1
    assert game._current_category == Category.SCIENCE

    game.places[game.current_player] = 5
    assert game._current_category == Category.SCIENCE

    game.places[game.current_player] = 9
    assert game._current_category == Category.SCIENCE

    game.places[game.current_player] = 2
    assert game._current_category == Category.SPORTS

    game.places[game.current_player] = 6
    assert game._current_category == Category.SPORTS

    game.places[game.current_player] = 3
    assert game._current_category == Category.ROCK

    game.places[game.current_player] = 7
    assert game._current_category == Category.ROCK

    game.places[game.current_player] = 10
    assert game._current_category == Category.SPORTS

    game.places[game.current_player] = 11
    assert game._current_category == Category.ROCK

def test_game_ask_question(init_game_with_players: Game):
    game = init_game_with_players

    # Position 0 is pop
    assert isinstance(game._ask_question(), str)

def test_game_roll_in_penalty_box(init_game_with_players: Game):
    game = init_game_with_players
    # Put player in penalty box
    game.in_penalty_box[game.current_player] = True

    # Odd roll that is more than 11
    ROLL = 13
    game.roll(ROLL)

    # Check that state is changed
    assert game.is_getting_out_of_penalty_box

    # Check the player has looped back to the start of the board
    assert game.places[game.current_player] == 1
     
    # Roll again an even
    ROLL = 2
    game.roll(ROLL)
    assert game.is_getting_out_of_penalty_box == False 

    # Still stuck in penalty box so not moving
    assert game.places[game.current_player] == 1


def test_game_roll_outside_penalty_box(init_game_with_players: Game):
    game = init_game_with_players
    # Put player in penalty box
    game.in_penalty_box[game.current_player] = False

    # Odd roll that is more than 11
    ROLL = 12
    game.roll(ROLL)

    # Check the player has looped back to the start of the board
    assert game.places[game.current_player] == 0