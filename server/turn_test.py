import unittest
from turn import Turn
from card import Card
from suit import Suit
from rank import Rank

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.a_turn = Turn(1, "maruko", Card(Suit.CLUB, Rank.ACE))

    def test_players(self):
        self.assertEqual(repr(self.a_turn), f"{{number: 1, player: maruko, card_added: {Card(Suit.CLUB, Rank.ACE)}}}")

if __name__ == "__main__":
    unittest.main()
