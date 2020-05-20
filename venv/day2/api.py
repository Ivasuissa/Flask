from flask import Flask, render_template, jsonify, json, request
from Flask.venv.day2.classes.intruments import GetInstruments, addInstrument, addKeyToInstrument
from Flask.venv.day2.classes.users import GetUser, addUser, deleteUser

app = Flask(__name__)

@app.route('/instruments')
def get_instruments():
    response = app.response_class(
        response=json.dumps(GetInstruments()),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users')
def get_users():
    response = app.response_class(
        response=json.dumps(GetUser()),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/add/instruments/<instrument_type>', methods=["GET", "POST"])
def add_instruments(instrument_type):
    addInstrument({"type": instrument_type})
    response = app.response_class(
        response=json.dumps({"type": instrument_type}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/add/user/<name>', methods=["GET", "POST"])
def add_user(name):
    addUser({"name": name})
    response = app.response_class(
        response=json.dumps({"name": name}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/instruments/<instrument_id>/users/<user_id>', methods=["GET", "POST"])
def add_instrument_to_users(instrument_id, user_id):
    instruments = GetInstruments()
    users = GetUser()
    if instrument_id in instruments.keys() and user_id in users.keys():
        addKeyToInstrument("user_id", user_id, instrument_id)
    response = app.response_class(
        response=json.dumps({'user_id': user_id, "id": instrument_id}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/users/<user_id>', methods=["GET", "POST"])
def get_instruments_by_user_id(id):
    instruments = GetInstruments()
    newDictionnarie = {}
    for instrument in instruments.values():
        if instrument["user_id"] == id:
            newDictionnarie[instrument["id"]] = instrument
    response = app.response_class(
        response=json.dumps(newDictionnarie),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/<link>/instruments/<id_instruments>', methods=["GET", "POST"])
def add_video_to_Instrument(id_instrument):
    link = request.args.get("link")
    instruments = GetInstruments()
    if id_instrument in instruments.keys():
        addKeyToInstrument("link", link, id_instrument)

    response = app.response_class(
        response=json.dumps({id_instrument: link}),
        status=200,
        mimetype='application/json'
    )
    return response





if __name__ == "__main__":
     app.run()