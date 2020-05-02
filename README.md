# Dhyut-Server

This is a server for round based card games that require everyone to add a card in a round.

The server exposes a few endpoints and websockets.

## API

## Ways to extend

- Add persistence. Currently data is saved in memory and mutations are not thread safe
- Do some cheating detection and prevent invalid moves (such as player adding card twice or more in a single round)
- Add input validation. The source has some basic unit tests but it is far from perfect
- Make PUT calls idempotent
- Make the API RESTful. Currently, the control commands are implemented as PUT calls, which is not RESTful. One way to fix it is to make control commands websocket based
- Containerize the server
- Make this more general purpose to be able to play any card game
- Make this general purpose so that it can work for any turn based game
- Make this repo follow a standard project structure. See [Flask, for example](https://github.com/pallets/flask).

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

