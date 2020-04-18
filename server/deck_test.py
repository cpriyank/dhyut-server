import unittest
from deck import Deck

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.a_deck = Deck()

    def test_initialization(self):
        self.assertEqual(len(self.a_deck.get_cards()), 52)

    def test_size(self):
        self.assertEqual(self.a_deck.size(), 52)

    def test_least_valued_card_removal(self):
        self.a_deck.remove_least_valued_n_cards(8)
        contains_twos = any(card.rank.value == "2" for card in self.a_deck.get_cards())
        contains_threes = sum(card.rank.value == "3" for card in self.a_deck.get_cards())
        contains_fours = sum(card.rank.value == "4" for card in self.a_deck.get_cards())
        self.assertFalse(contains_twos)
        self.assertEqual(contains_threes, 1)
        self.assertEqual(contains_fours, 3)

    def test_repeated_card_removal(self):
        self.a_deck.remove_least_valued_n_cards(4)
        contains_threes = sum(card.rank.value == "3" for card in self.a_deck.get_cards())
        self.assertEqual(contains_threes, 4)
        self.a_deck.remove_least_valued_n_cards(4)
        contains_threes = sum(card.rank.value == "3" for card in self.a_deck.get_cards())
        contains_fours = sum(card.rank.value == "4" for card in self.a_deck.get_cards())
        self.assertEqual(contains_threes, 1)
        self.assertEqual(contains_fours, 3)

if __name__ == "__main__":
    unittest.main()
