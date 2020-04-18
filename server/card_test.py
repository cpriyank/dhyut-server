import unittest
from suit import Suit
from rank import Rank
from card import Card

class TestCardMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE))

if __name__ == "__main__":
    unittest.main()

