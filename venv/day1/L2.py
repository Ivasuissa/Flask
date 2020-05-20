from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/api/instruments/')
def create_musical_instrument():
    dictionnaire = {
        'instrument': 'guitare',
        'users': 'Eva',
        'id': '1',
    }
    return jsonify(dictionnaire)


#if __name__ == "__main__":