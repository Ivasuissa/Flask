from flask import Flask, render_template, jsonify, json
import random
import string

app = Flask(__name__)

instruments = []

class Instruments:
    def __init__(self,instrument):
        self.type = instrument["type"]
        self.id = get_random_alphaNumeric_string()
        self.user_id = "none"
        self.linkVideo = 'none'

    def BuildInstrumentDictionary(self):
        dictionary= json.dumps(self.__dict__)
        return dictionary

def get_random_alphaNumeric_string(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join((random.choice(letters) for i in range(stringLength)))

def GetInstruments():
    print(instrumentsList)
    return instrumentsList

instrumentsList = {}

def addInstrument(instrument):
    newInstrument = Instruments(instrument)
    instrument_add = json.loads(newInstrument.BuildInstrumentDictionary())
    instrumentsList[instrument_add['id']] = instrument_add
    print(instrumentsList)

def addKeyToInstrument(key, value, instrument_id):
    instrumentsList[instrument_id][key] = value

