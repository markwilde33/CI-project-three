import os
from flask import Flask, render_template, flash, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired
import json

app = Flask(__name__)
# ///Set Database variables///
USER_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/users.json')
LEADERBOARD_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/leaderboard.json')
ANIMAL_RIDDLE_DATABASE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/animal_riddles.json')

# Set quiz rules
MAX_ATTEMPT = 3
CORRECT_SCORE = 5
INCORRECT_SCORE = -1

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


# retrieve users
def get_users():
    users = {}
    with open(USER_DATABASE) as reader:
        users = json.load(reader)
    return users


class RegisterForm(Form):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# route to and logic for the registration page


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = form.password.data
        registered_users = get_users()
        if not any(registered_user['username'].lower() == name.lower() for registered_user in registered_users['users']):
            registered_users['users'].append(
                {'username': name, 'password': password})
            with open(USER_DATABASE, 'w') as writer:
                json.dump(registered_users, writer)
            flash(
                'Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose another name.', 'warning')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)

# route to and logic for the login page


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        post_username = request.form['username']
        post_password = request.form['password']
        is_authenticated = False
        registered_users = get_users()
        for entry in registered_users['users']:
            if entry['username'] == post_username:
                if entry['password'] == post_password:
                    is_authenticated = True
                    session['logged_in'] = True
                    session['name'] = entry['username']
                    session['index'] = 0
                    session['attempt'] = MAX_ATTEMPT
                    session['score'] = 0
                    flash('You are now logged in', 'success')
                    return redirect(url_for('start_quiz'))
                else:
                    error = 'Invalid Password'
                    return render_template('login.html', error=error)
        if not is_authenticated:
            error = 'Username does not exist'
            return render_template('login.html', error=error)
    return render_template('login.html')


# route to logout and return to login page
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# route to the  start quiz page
@app.route('/start_quiz')
def start_quiz():
    return render_template('start_quiz.html')


if __name__ == '__main__':
    initialize()
    app.secret_key = 'secret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
