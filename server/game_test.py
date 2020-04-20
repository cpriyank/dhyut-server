import unittest
from game import Game
from deck import Deck

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.a_game = Game()
        self.number_of_players = 7
        self.players = []
        for i in range(self.number_of_players):
            self.players.append(self.a_game.add_player(str(i)))

    def test_players(self):
        self.assertEqual(len(self.a_game.get_players()), self.number_of_players)

    def test_card_adjustment(self):
        cards = self.a_game.adjust_number_of_cards_for_players([Deck(), Deck()], self.number_of_players)
        # total 104 cards, 7 players, each will get 14, discarding 6
        self.assertEqual(len(cards), 98)

    def test_card_distribution(self):
        cards = self.a_game.adjust_number_of_cards_for_players([Deck(), Deck()], self.number_of_players)
        self.a_game.distribute_cards(cards)
        self.assertTrue(all(len(player.cards) == 14) for _, player in self.a_game.players.items())
        total_cards = sum(1 for _, player in self.a_game.players.items() for card in player.cards)
        self.assertEqual(total_cards, 98)

    def test_player_move_without_a_round(self):
        cards = self.a_game.adjust_number_of_cards_for_players([Deck(), Deck()], self.number_of_players)
        self.a_game.distribute_cards(cards)
        player_id, player = next(iter(self.a_game.players.items())) # just get a random player
        card = player.cards[-1]
        self.a_game.add_player_move(player_id, str(card))
        # TODO: separate tests
        self.assertEqual(13, len(player.cards))
        self.assertEqual(card, player.card_added)
        turn = self.a_game.rounds[-1][-1]
        self.assertEqual(turn.card_added, player.card_added)
        self.a_game.undo_move()
        self.assertEqual(14, len(self.a_game.players[player_id].cards))
        self.assertEqual(len( self.a_game.rounds[-1].turns ), 0)

if __name__ == "__main__":
    unittest.main()
