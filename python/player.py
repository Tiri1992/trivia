class Player:
    
    def __init__(self, name: str, place: int) -> None:
        self._name = name 
        self._place = place
        self._purses = 0 
        self._in_penalty_box = False 

    def __str__(self) -> str:
        return f"Player: {self._name}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def place(self) -> int:
        return self._place

    @property
    def in_penalty_box(self) -> bool:
        return self._in_penalty_box

    def add_purse(self) -> None:
        self._purses += 1

    def move_in_penalty_box(self) -> None:
        self._in_penalty_box = True 

    def move_out_penalty_box(self) -> None:
        self._in_penalty_box = False 

    def move_place(self, count: int) -> None:
        self._place = (self._place + count) % 12

    def display_coins(self) -> str:
        return f"{self} now has {self._purses} Gold Coins."

    def display_place(self) -> str:
        return f"{self} new location is {self._place}"

    def display_in_penalty_box(self) -> str:
        return f"{self} was sent to the penalty box"

    def has_won(self) -> bool:
        return not (self._purses == 6)
