from flask import Flask, json
import requests
import datetime

app = Flask(__name__)

class BasePost:
   def __init__(self, post):
       self.userId = post['userId']
       self.id = post['id']
       self.title = post['title']
       self.body = post['body']

class ExtendedPost(BasePost):

    def __init__(self, post):
        super().__init__(post)
        self.createdAt = str(datetime.datetime.now())

class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def get_posts(self, url):
        url = 'https://jsonplaceholder.typicode.com/posts/'
        data_response = requests.get(url)
        if data_response.status_code != 200:
            abort(404)

        data = data_response.json()
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json',
        )
        for i in data:
            post = i;
            print(post)




user = JsonablePost()
post = user.get_post()



