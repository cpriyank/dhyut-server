from flask.json import JSONEncoder
from card import Card
from player import Player


class GameObjectsEncoder(JSONEncoder):
    @staticmethod
    def jsonify_cards(cards):
        return list(map(str, cards))

    def default(self, obj):  # pylint: disable = E0202
        if isinstance(obj, Player):
            return {
                "id": obj.id,
                "name": obj.name,
                "card_added": obj.card_added,
                # TODO: this is a hack
                "cards": GameObjectsEncoder.jsonify_cards(obj.cards),
                "card_won": GameObjectsEncoder.jsonify_cards(obj.card_won),
            }
        return super(GameObjectsEncoder, self).default(obj)
