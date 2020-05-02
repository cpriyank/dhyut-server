# Dhyut-Server

This is a server for round based card games that require everyone to add a card in a round.
For rapid prototyping, this is written in Python with flask.

The server exposes a few endpoints and websockets.

## REST API

All responses are jsonified.

### GET endpoints

#### /ping

Pings the server

#### /players

Returns a list of player object

### PUT endoints

Currently, there's no check for idempotence. [Read more on why it should be.](https://restfulapi.net/idempotent-rest-apis/)

#### /players/<player_name>

Register player with `player_name`

#### /rounds/winner/<player_id>

Declares `player_id` as winner

#### /rounds/current/undo

Undo last move and broadcasts update via websocket via `updateCardView` event.

#### /game/start

Takes `number_of_decks` as json payload.

Broadcasts update via websocket via `updateCardView` event.

### POST endoints

#### /players/<player_id>

Takes text representation of card as a payload. Sample `{ card: ♥A}`

### DELETE endpoints

#### /players/<player_id>

Unregister a player.

### Socket endpoints

#### `pingServer` event

Returns a message via `messageChannel` event.

## Ways to contribute

- Add persistence. Currently data is saved in memory and mutations are not thread safe
- Do some cheating detection and prevent invalid moves (such as player adding card twice or more in a single round)
- Add input validation. The source has some basic unit tests but it is far from perfect
- Throw relevant [HTTP Status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) to clients on client and server errors with custom messages
- Make PUT calls idempotent
- Make the API RESTful. Currently, the control commands are implemented as PUT calls, which is not RESTful. One way to fix it is to make control commands websocket based
- Containerize the server
- Make this more general purpose to be able to play any card game
- Make this general purpose so that it can work for any turn based game
- Make this repo follow a standard project structure. See [Flask, for example](https://github.com/pallets/flask).
- Make API endpoint structure more intuitive and consistent.
- Write documentation with a proper documentation generator. [Sphinx](for example).

## Running

It'd be good to create a python virtual environment and switch to it

Make sure you have python3 installed.

From within the `server` dir, run

```bash
pip install -r requirements.txt
```

This will install `flask` and its dependencies.

To run,

```bash
python3 app.py
```

This will run the server on `localhost:5000`

A basic frontend that works with this is implemented [here](github.com/cpriyank/dhyut-client)

