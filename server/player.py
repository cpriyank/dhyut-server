import uuid

class Player:
    def __init__(self, name=''):
        self.name = name
        self.id = uuid.uuid4().hex
        self.card_added = None
        self.cards = []
        self.card_won = []
        # TODO: Add point calculation logic
        # self.points = 0

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        # allow players with same name
        return self.id == other.id

    # required to make a type hashable to create a set, dict, etc out of it.
    def __hash__(self):
        return hash(f'{self.name}{self.id}')

    def __repr__(self):
        return f'{self.name}'

    def initialize_cards(self, initial_cards):
        self.cards = initial_cards

    def put_card(self, card):
        self.card_added = card
        self.cards.remove(card)

    def undo_put_card(self, card):
        self.cards.append(card)

    def add_cards_to_cards_won(self, cards):
        self.card_won.extend(cards)
        # TODO: Update points


