import unittest
from player import Player
from card import Card

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.a_player = Player("sweet")

    def test_initialization(self):
        card = Card("heart", 1)
        self.a_player.initialize_cards([card])
        self.assertEqual(self.a_player.cards.pop(), card)

    def test_put_card(self):
        card = Card("heart", 1)
        self.a_player.initialize_cards([card])
        self.a_player.put_card(card)
        self.assertFalse(self.a_player.cards)
        self.assertEqual(self.a_player.card_added, card)

if __name__ == "__main__":
    unittest.main()
