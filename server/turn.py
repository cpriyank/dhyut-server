class Turn:
    def __init__(self, number, player, card_added=None):
        self.number = number
        self.player = player
        self.card_added = card_added

    def __eq__(self, other):
        if not isinstance(other, Turn):
            return NotImplemented
        # we don't check for card_added, which is going to be mutated in a turn
        return self.player == other.player

    # TODO: repr is not a good way to serialize
    def __repr__(self):
        return f'{{number: {self.number}, player: {self.player.name}, card_added: {self.card_added}}}'
