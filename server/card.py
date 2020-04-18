class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    # required to make a type hashable to create a set, dict, etc out of it.
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f'{self.suit.value}{self.rank.value}'
