import os
from flask import Flask, render_template

app = Flask(__name__)

# route to index page


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
