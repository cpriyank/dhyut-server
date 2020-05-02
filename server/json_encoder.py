from flask.json import JSONEncoder
from flask import Flask, jsonify, request
from player import Player
from card import Card
from suit import Suit
from rank import Rank
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


class CustomPlayerEncoder(json.JSONEncoder):
    def default(self, obj):  # pylint: disable = E0202
        if isinstance(obj, Card):
            return str(obj)
        if isinstance(obj, Player):
            return {
                "id": obj.id,
                "name": obj.name,
                "card_added": obj.card_added,
                # TODO: this is a hack
                "cards": obj.cards,
                "cards_won": obj.cards_won,
            }
        return super(CustomPlayerEncoder, self).default(obj)


class GameObjectsEncoder(JSONEncoder):
    @staticmethod
    def jsonify_cards(cards):
        return list(map(str, cards))

    def default(self, obj):  # pylint: disable = E0202
        if isinstance(obj, Card):
            return str(obj)
        if isinstance(obj, Player):
            return {
                "id": obj.id,
                "name": obj.name,
                "card_added": obj.card_added,
                # TODO: this is a hack
                "cards": obj.cards,
                "cards_won": obj.cards_won,
            }
        return super(GameObjectsEncoder, self).default(obj)


# TODO: Following is poor man's way to test the API response json
app.json_encoder = GameObjectsEncoder
player = Player("magan", 123, Card(Suit.CLUB, Rank.ACE),
                [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE)],
                [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE)])
player2 = Player("madan", 1234, Card(Suit.CLUB, Rank.ACE),
                 [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE)],
                 [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE)])

players = [player, player2]


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify(players)


if __name__ == '__main__':
    app.run()
