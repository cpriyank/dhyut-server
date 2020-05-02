from itertools import islice
from random import shuffle

from card import Card
from deck import Deck
from player import Player
from round import Round


class Game:
    def __init__(self):
        # player is an object that will contain cards as well
        # we do not maintain a separate property for cards
        # TODO: maintain a separate storage class
        self.players = {}
        self.rounds = []

    def add_player(self, player_name):
        player = Player(player_name)
        self.players[player.id] = player
        return player

    def remove_player(self, player_id):
        self.players.pop(player_id)

    def get_players(self):
        return self.players

    def declare_current_round_winner(self, player_id):
        if self.rounds:
            if not len(self.rounds[-1].turns) == len(self.players):
                raise ValueError("not all the players have finished")
            self.players[player_id].add_cards_to_cards_won(
                list(turn.card_added for turn in self.rounds[-1])
            )
            return self.players[player_id]
        else:
            # TODO: throw error instead?
            print("tried to declare winner without a round")

    # TODO: Currently, there's no automated guard against player adding card twice
    def add_player_move(self, player_id, card_text):
        if not self.rounds:
            self.rounds.append(Round())
        player = self.players[player_id]
        card = Card.from_text(card_text)
        self.players[player_id].put_card(card)
        self.rounds[-1].add_turn(player, card)
        # if everyone added cards, prepare for a new round
        if len(self.rounds[-1].turns) == len(self.players):
            self.rounds.append(Round())

    def undo_move(self):
        # TODO: log else clause
        if self.rounds:
            turn = self.rounds[-1].undo_turn()
            player_id = turn.player.id
            self.players[player_id].undo_put_card(turn.card_added)

    @staticmethod
    def adjust_number_of_cards_for_players(decks, number_of_players):
        total_cards = sum(deck.size() for deck in decks)
        # assumes number_of_players is non zero
        number_of_cards_to_discard = total_cards % number_of_players
        number_of_cards_to_remove_from_all_decks = number_of_cards_to_discard // len(
            decks
        )
        all_but_initial_decks = (
            deck.remove_least_valued_n_cards(number_of_cards_to_remove_from_all_decks)
            for deck in decks[1:]
        )
        number_of_additional_cards_to_remove_from_a_deck = (
            number_of_cards_to_discard % len(decks)
        )
        decks = list(all_but_initial_decks) + [
            decks[0].remove_least_valued_n_cards(
                number_of_cards_to_remove_from_all_decks
                + number_of_additional_cards_to_remove_from_a_deck
            )
        ]
        return [card for deck in decks for card in deck]

    def distribute_cards(self, cards):
        """
        At this point, len(cards) % len(self.players) is 0 and cards are well
        shuffled
        """
        number_of_cards_per_player = len(cards) // len(self.players)
        cards = iter(cards)
        for _, player in self.players.items():
            player.initialize_cards(list(islice(cards, number_of_cards_per_player)))

    def prepare_cards_for_distribution(self, number_of_decks):
        # assumes self.players is initialized
        decks = [Deck() for _ in range(number_of_decks)]
        cards = self.adjust_number_of_cards_for_players(decks, len(self.players))
        # as an exercise, implement your own O(n) shuffle function based on fisher-yates-knuth shuffle
        shuffle(cards)
        return cards
