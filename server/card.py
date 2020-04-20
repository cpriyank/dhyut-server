from suit import Suit
from rank import Rank

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @staticmethod
    def from_text(text):
        text = text.strip()
        suit_value, rank_value = text[0], text[1]
        # TODO: how inefficient is this?
        suit = next(filter(lambda a_suit: a_suit.value == suit_value, Suit))
        rank = next(filter(lambda a_rank: a_rank.value == rank_value, Rank))
        return Card(suit, rank)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    # required to make a type hashable to create a set, dict, etc out of it.
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f'{self.suit.value}{self.rank.value}'

    def __str__(self):
        return f'{self.suit.value}{self.rank.value}'
