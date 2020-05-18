from flask import Flask, json
import requests
import json

app = Flask(__name__)


@app.route('/data')
def get_posts(website):
    data_response = requests.get(website)
    if data_response.status_code == 200:
        print('There is a 200 response code')

    else:
        print ('There is no 200 response code')


get_posts('https://www.ynet.co.il')
get_posts('https://www.itc.tech')
get_posts('https://main.knesset.gov.il')