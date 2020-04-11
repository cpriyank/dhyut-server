# kalitiri
Full stack application for કાળી તીરી

## Server side

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

## Client side

Make sure you have node and `npm` installed.

`cd` to `client` directory and run `npm install`. More than necessary
dependencies are defined in `package.json`, some will be removed in future.

`npm run serve` should build the frontend and run on `localhost:8080/play`
