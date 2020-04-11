import uuid
from player import Player
from game import Game
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

game = Game()

def add_player(name):
    player = Player(name)
    game.add_player(player.__dict__)
    return player

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/players', methods=['GET'])
def all_players():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object['players'] = game.players
    return jsonify(response_object)

@app.route('/players/<player_id>', methods=['GET', 'POST', 'PUT'])
def control_player(player_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        post_data = request.get_json()
        response_object['message'] = 'Book updated!'
        response_object['cards'] = ["A2", "B3"]
        response_object['cards_won'] = ["A2", "B3"]
    elif request.method == 'POST':
        response_object['message'] = 'Book updated!'
        post_data = request.get_json()
    elif request.method == 'PUT':
        player = add_player(player_id)
        response_object['playerId'] = player.id
        response_object['players'] = game.players
        response_object['message'] = 'registered'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()