import os
import json
from flask import Flask, render_template, flash, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired
from functools import wraps

app = Flask(__name__)
# Set the variable names for the path to the json files
USERS = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/users.json')
LEADERBOARD = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/leaderboard.json')
RIDDLES = os.path.join(os.path.dirname(
    os.path.abspath(__file__)) + '/data/animal_riddles.json')

# Set quiz rules
MAX_ATTEMPT = 3
CORRECT_SCORE = 5
INCORRECT_SCORE = -1

# Riddles list
animal_riddles = []


def initialize():
    # write to users.json
    if not os.path.exists(USERS):
        data = {'users': []}
        with open(USERS, 'w') as writer:
            json.dump(data, writer)
    # write to leaderboard.json
    if not os.path.exists(LEADERBOARD):
        data = {'leaders': []}
        with open(LEADERBOARD, 'w') as writer:
            json.dump(data, writer)
    # Read from the animal_riddles.json
    global animal_riddles
    with open(RIDDLES) as reader:
        animal_riddles = json.load(reader)


def get_users():
    # retrieve users from users.json
    users = {}
    with open(USERS) as reader:
        users = json.load(reader)
    return users


def get_question():
    # retrieve questions from animal_riddles.json
    return 'Question ' + str(session['index'] + 1) + ':  ' + animal_riddles[session['index']]['riddle']


def get_answer():
    # retrieve answers from animal_riddles.json
    return 'Answer ' + ': ' + animal_riddles[session['index']]['answer']


def get_image():
     # retrieve images from animal_riddles.json
    return animal_riddles[session['index']]['image_source']


def get_links():
    # retrieve animal info links from animal_riddles.json
    return animal_riddles[session['index']]['links']


def get_leaders():
     # retrieve leaders from leaderboard.json
    leaders = {}
    with open(LEADERBOARD) as reader:
        leaders = json.load(reader)
    return leaders


def update_leaderboard():
# update the leaderboard when user completes the quiz
    existing_leaders = get_leaders()
    existing_leaders['leaders'].append({'username':session['name'], 'score':session['score']})
    with open(LEADERBOARD, 'w') as writer:
        json.dump(existing_leaders, writer)


@app.route('/')
# route to index page
@app.route('/index')
def index():
    return render_template('index.html')


class RegisterForm(Form):
    # Simple wtform for user registration
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


@app.route('/register', methods=['GET', 'POST'])
# route to and logic for the registration page
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = form.password.data
        registered_users = get_users()
        if not any(registered_user['username'].lower() == name.lower() for registered_user in registered_users['users']):
            registered_users['users'].append(
                {'username': name, 'password': password})
            with open(USERS, 'w') as writer:
                json.dump(registered_users, writer)
            flash(
                'Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose another name.', 'warning')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
# route to and logic for the login page
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


def is_logged_in(f):
    # wrapper function to ensure the user is logged in before having access to the quiz, found at: https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash(
                'You are unauthorized to perform this action. Please register and/or login first', 'danger')
            return redirect(url_for('register'))
    return wrap


@app.route('/logout')
# route to logout and return to login page
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))


@app.route('/start_quiz')
# route to the  start quiz page
@is_logged_in
def start_quiz():
    return render_template('start_quiz.html')


@app.route('/play_quiz', methods=['GET'])
# route to play the quiz
@is_logged_in
def play_quiz():
    return render_template('play_quiz.html', question = get_question())


@app.route('/riddle', methods=['POST'])
# Route to loop through the riddles and quiz scoring logic
@is_logged_in
def riddle():
    if request.method == 'POST':
        answer = request.form['answer']
        correct_answer = None
        last_question = None
        if animal_riddles[session['index']]['answer'].lower() == answer.lower():
            if session['index'] != len(animal_riddles) - 1:
                flash('Well done! That is correct.', 'success')
            session['score'] += CORRECT_SCORE
            correct_answer = True
        elif session['attempt'] == 1:
            session['score'] += INCORRECT_SCORE
            if session['index'] != len(animal_riddles) - 1:
                flash('Hard luck!. Try the next riddle.', 'danger')
                session['index'] += 1
                session['attempt'] = MAX_ATTEMPT
            else:
                return next_question()    
        else:
            session['attempt'] -= 1
            session['score'] += INCORRECT_SCORE
            flash('"' + answer + '" is an incorrect answer. '+ str(session['attempt']) +' attempts remaining', 'warning')
        if session['index'] == len(animal_riddles) - 1:
            last_question = True
        return render_template('play_quiz.html', question = get_question(), correct_answer = correct_answer, answer = get_answer(), image = get_image(), last_question = last_question, links = get_links())


@app.route('/next_question', methods=['POST'])
# Route to next question and logic for displaying the next question 
@is_logged_in
def next_question():
    if request.method == 'POST':
        session['index'] += 1
        session['attempt'] = MAX_ATTEMPT
        if session['index'] == len(animal_riddles):
            update_leaderboard()
            flash('You have completed the Quiz. Your score is ' + str(session['score']), 'success')
            session['index'] = 0
            session['score'] = 0
            return render_template('start_quiz.html')
        else:
            return render_template('play_quiz.html', question = get_question())


@app.route('/leaderboard', methods=['GET'])
# Route to and logic for riddle leaderboard. Show top ten user scores.
@is_logged_in
def leaderboard():
    existing_leaders = get_leaders()['leaders']
    sorted_leaders = sorted(existing_leaders, key = lambda i : (i['score']), reverse=True)
    return render_template('leaderboard.html', leaders = sorted_leaders[:10])


if __name__ == '__main__':
    initialize()
    app.secret_key = 'secret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)