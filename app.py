import os
from flask import Flask, render_template
import json

app = Flask(__name__)
# ///Set Database variables///
USER_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/users.json')
LEADERBOARD_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/leaderboard.json')
ANIMAL_RIDDLE_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/animal_riddles.json')


# ///Riddles list///
animal_riddles = []

# ///write to user and leaderboard databases///


def initialize():
    # ///write to the user and database///
    if not os.path.exists(USER_DATABASE):
        data = {'users': []}
        with open(USER_DATABASE, 'w') as writer:
            json.dump(data, writer)
    # ///write to the leaderboard database///
    if not os.path.exists(LEADERBOARD_DATABASE):
        data = {'leaders': []}
        with open(LEADERBOARD_DATABASE, 'w') as writer:
            json.dump(data, writer)
    # ///Read from the riddle database///
    global animal_riddles
    with open(ANIMAL_RIDDLE_DATABASE) as reader:
        animal_riddles = json.load(reader)


# ///route to index page///
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    initialize()
    app.secret_key = 'secret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
