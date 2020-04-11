import uuid

class Player:
    def __init__(self, name=''):
        self.name = name
        self.id = uuid.uuid4().hex
