from turn import Turn
from itertools import count

class Round:
    """
    A round is a list of turns
    """
    def __init__(self):
        self.turn_number_generator = 0
        self.turns = []

    def __iter__(self):
        return iter(self.turns)

    def __getitem__(self, key):
        """
        Allow accessing turns by indexing; round[0] will give zeroth turn
        """
        return self.turns[key]

    def add_turn(self, player, card):
        turn = Turn(self.turn_number_generator + 1, player.name, card)
        if not any(existing_turn == turn for existing_turn in self.turns):
            self.turn_number_generator += 1
            self.turns.append(turn)

    def undo_turn(self):
        """
        Allow undoing last turn
        """
        if self.turns:
            self.turn_number_generator -= 1
            return self.turns.pop()
