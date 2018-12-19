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


# ///route to index page///
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
