import uuid
from player import Player
from game import Game
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from json_encoder import GameObjectsEncoder
from invalid_usage import InvalidUsage

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.json_encoder = GameObjectsEncoder

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(app, cors_allowed_origins="*")

game = Game()

# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


################################################################################
# Admin endpoints
# TODO: Control commands are not restful
################################################################################
@app.route("/rounds/winner/<player_id>", methods=["PUT"])
def declare_current_winner(player_id):
    response_object = {"status": "success"}
    game.declare_current_round_winner(player_id)
    return jsonify(response_object)


@app.route("/rounds/current/undo", methods=["PUT"])
def undo_last_move():
    response_object = {"status": "success"}
    game.undo_move()
    return jsonify(response_object)


@app.route("/game/start", methods=["PUT"])
def distribute_cards():
    response_object = {"status": "success"}
    request_data = request.get_json()
    print(request_data)
    if not request_data:
        # TODO magic strings
        raise InvalidUsage(
            "You must supply number_of_decks in payload", status_code=405
        )
    number_of_decks = int(request_data["number_of_decks"])
    # TODO: only expose one function from game to distribute cards
    cards = game.prepare_cards_for_distribution(number_of_decks)
    game.distribute_cards(cards)
    return jsonify(response_object)


################################################################################
# Player endpoints
################################################################################
@app.route("/players", methods=["GET"])
def all_players():
    response_object = {"status": "success"}
    if request.method == "GET":
        response_object["players"] = game.get_players()
    return jsonify(response_object)


# TODO: error handling can be improved
@app.route("/players/<player_id>", methods=["DELETE", "POST", "PUT"])
def control_player(player_id):
    response_object = {"status": "success"}
    if request.method == "POST":
        request_data = request.get_json()
        card_text = request_data["card"]
        game.add_player_move(player_id, card_text)
    elif request.method == "PUT":
        # this is called when a player joins the game
        player = game.add_player(player_id)
        response_object["playerId"] = player.id
        response_object["players"] = game.get_players()
    elif request.method == "DELETE":
        game.remove_player(player_id)
    return jsonify(response_object)


################################################################################
# Socket endpoints
################################################################################
@socketio.on("messageChannel")
def test_message(message):
    emit("messageChannel", {"data": "got it!"})


# when all the players have joined, admin can call this socket channel to indicate
# start of the game. This will broadcast list of players joined.
@socketio.on("startGame")
def start_game(number_of_decks):
    game.distribute_cards(number_of_decks)
    emit("gameStarted", game.get_players())


@socketio.on("pingServer")
def test_message(message):
    print(f"received {message}")
    emit("messageChannel", {"data": "got it!"})


if __name__ == "__main__":
    socketio.run(app)
