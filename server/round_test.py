import unittest
from round import Round
from player import Player
from card import Card
from suit import Suit
from rank import Rank
from itertools import islice, product


class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.a_round = Round()
        self.players = [Player(i) for i in range(5)]
        # exercise for reader: understand how generators and iterators work; learn their
        # benefits and drawbacks
        self.cards = (Card(suit, rank) for rank, suit in islice(product(Rank, Suit), 10))

    # TODO: Improve tests
    # ideally, each test should test only one behavior
    def test_many_things(self):
        self.a_round.add_turn(self.players.pop(), next(self.cards))
        self.a_round.add_turn(self.players.pop(), next(self.cards))
        self.a_round.add_turn(self.players.pop(), next(self.cards))
        self.assertEqual(self.a_round[2].number, 3)
        undoed_turn = self.a_round.undo_turn()
        self.assertEqual(undoed_turn.number, 3)
        self.assertEqual(undoed_turn.player.name, 2)


if __name__ == "__main__":
    unittest.main()
