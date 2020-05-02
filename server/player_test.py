import unittest
from player import Player
from card import Card
import json


class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.player_1_name = "sweet"
        self.player_2_name = "sour"
        self.a_player = Player(self.player_1_name)
        self.another_player = Player(self.player_2_name)

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

    def test_serialization(self):
        players = [self.a_player, self.another_player]
        serialized = json.dumps(self.a_player)
        self.assertTrue(json.loads(serialized)['name'] == self.player_1_name)
        to_dict_list = {"players": json.dumps([player.dict_form for player in players])}
        # print(to_dict_list['players'])
        serialized_list = json.dumps(to_dict_list)
        deserialized_list = json.loads(serialized_list)
        print(deserialized_list['players'])


if __name__ == "__main__":
    unittest.main()
