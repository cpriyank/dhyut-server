from suit import Suit
from card import Card
from rank import Rank
from itertools import product, filterfalse, count, islice

# requires understanding of python closures, generators, and iterators
class Deck:
    STANDARD_DECK_SIZE = 52
    def __init__(self):
        self.cards = [Card(suit, rank) for rank, suit in product(Rank, Suit)]

    def get_cards(self):
        return self.cards

    def size(self):
        return len(self.cards)

    def __iter__(self):
        # to iterate over a deck with expressions like `for card in deck`
        return iter(self.cards)

    # assumes that cards are ordered ♥2, ♠2, ♣ 2, ♦2, ♥3 , etc
    def remove_least_valued_n_cards(self, n, preserve = Card(Suit.SPADE, Rank.THREE), *more_cards_to_preserve):
        # we don't want to remove some cards, such as ♠3
        cards_to_preserve = set([preserve])
        cards_to_preserve.update(set(more_cards_to_preserve))
        safe_to_remove_deck = [card for card in self.cards if card not in cards_to_preserve]
        safe_to_remove_deck = safe_to_remove_deck[n:]
        self.cards = list(cards_to_preserve) + safe_to_remove_deck
        return self

# deck = Deck()
# print([card for card in deck.get_cards()])
