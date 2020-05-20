from flask import Flask, json
import requests

app = Flask(__name__)





@app.route('/data')
def get_posts():
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    if data_response.status_code != 200:
        abort(404)

    data = data_response.json()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response
get_posts()


@app.route('/data/<id>')
def get_posts_from_id(id):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + id)
    if data_response.status_code != 200:
        abort(404)


    data = data_response.json()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response
get_posts_from_id("1")

@app.route('/data/<userId>')
def get_posts_from_userId(userId):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + userId)
    if data_response.status_code != 200:
        abort(404)


    data = data_response.json()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response
get_posts_from_userId("1")






if __name__ == "__main__":
   app.run()
