import unittest
from suit import Suit
from rank import Rank
from card import Card

class TestCardMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE))

    def test_card_from_text(self):
        text = Suit.HEART.value + Rank.ACE.value
        card = Card.from_text(text)
        self.assertEqual(card, Card(Suit.HEART, Rank.ACE))

if __name__ == "__main__":
    unittest.main()

