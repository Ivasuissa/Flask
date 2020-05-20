from flask import Flask, render_template, jsonify, json
import random
import string
import requests
app = Flask(__name__)



class User():
    def __init__(self,user):
        self.name = user["name"]
        self.user_id = get_random_alphaNumeric_string()

    def BuildUserDictionaty(self):
        dictionary= json.dumps(self.__dict__)
        return dictionary

def get_random_alphaNumeric_string(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join((random.choice(letters) for i in range(stringLength)))

def GetUser():
    return usersList


usersList= {}

def addUser(user):
    newUser = User(user)
    user_add = json.loads(newUser.BuildUserDictionaty())
    usersList[user_add['user_id']]=user_add
    print(usersList)

