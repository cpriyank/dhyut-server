from collections import namedtuple

class Turn:
    def __init__(self, number, player_name, card_added=None):
        self.number = number
        # player is a big object, we don't want to transport it during every turn,
        # so we just save the name
        self.player_name = player_name
        self.card_added = card_added

    def __eq__(self, other):
        if not isinstance(other, Turn):
            return NotImplemented
        # we don't check for card_added, which is going to be mutated in a turn
        return self.player_name == other.player_name

    # TODO: repr is not a good way to serialize
    def __repr__(self):
        return f'{{number: {self.number}, player: {self.player_name}, card_added: {self.card_added}}}'
