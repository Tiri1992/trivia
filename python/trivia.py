from category import Category, position_category
from errors import NotEnoughPlayersError
from player import Player
from questions import Question

class Game:
    def __init__(self, players: list[Player]):
        self._players = players
        self._current_player_index = 0

        self._pop_questions = Question.from_pop(total=50)  
        self._science_questions = Question.from_science(total=50)
        self._sports_questions = Question.from_sport(total=50)
        self._rock_questions = Question.from_rock(total=50)


    def create(self) -> None:
        if not self.is_playable():
            raise NotEnoughPlayersError(f"Insufficient players to create game. Total players must be greater than 2, currently at {len(self._players)}")
        self._pop_questions.create()
        self._science_questions.create()
        self._sports_questions.create()
        self._rock_questions.create()

    @property
    def current_player(self) -> Player:
        return self._players[self._current_player_index]
    
    def is_playable(self) -> bool:
        return self.get_number_of_players() >= 2

    def get_number_of_players(self) -> int:
        return len(self._players)
    
    def roll(self, roll):
        print("%s is the current player" % self.current_player)
        print("They have rolled a %s" % roll)
        
        if self.current_player.in_penalty_box:
            if roll % 2 != 0:
                print("%s is getting out of the penalty box" % self.current_player)
                self.current_player.move_place(count=roll)
                print(self.current_player.display_place())
                print("The category is %s" % self._current_category)
                self._ask_question()
                self.current_player.move_out_penalty_box()
            else:
                print("%s is not getting out of the penalty box" % self.current_player)
                
        else:
            self.current_player.move_place(count=roll)
            print(self.current_player.display_place())
            print("The category is %s" % self._current_category)
            self._ask_question()
    
    def _ask_question(self):
        if self._current_category is Category.POP: 
            return self._pop_questions.get_question()
        if self._current_category is Category.SCIENCE: 
            return self._science_questions.get_question()
        if self._current_category is Category.SPORTS: 
            return self._sports_questions.get_question()
        if self._current_category is Category.ROCK: 
            return self._rock_questions.get_question()
        
    
    @property
    def _current_category(self) -> str | None:
        return position_category.get(self.current_player.place)

    def was_correctly_answered(self) -> Player:
        if not self.current_player.in_penalty_box:
            print('Answer was correct!!!!')
            self.current_player.add_purse()
            self.current_player.display_coins()
            winner = self.current_player.has_won()
            self.next_player()                
            return winner
        print(f"{self.current_player} still in penalty box.")
    
    def next_player(self) -> None:
        self._current_player_index = (self._current_player_index + 1) % self.get_number_of_players()
    
    def wrong_answer(self):
        if not self.current_player.in_penalty_box:
            print('Question was incorrectly answered')
            print(self.current_player.display_in_penalty_box())
            self.current_player.move_in_penalty_box()
            self.next_player()
            return True
        return False

    def get_players_in_penalty_box(self) -> list[Player]:
        return [player for player in self._players if player.in_penalty_box]



if __name__ == '__main__':
    from random import randrange
    
    not_a_winner = False

    players = [ 
        Player(name="Chet", place=0),
        Player(name="Pat", place=0),
        Player(name="Sue", place=0),
    ]

    game = Game(players=players)
    game.create()

    while True:
        game.roll(randrange(5) + 1)
        # First Wrong Answer, will break out of loop
        if randrange(5) == 2:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        if not not_a_winner: break
