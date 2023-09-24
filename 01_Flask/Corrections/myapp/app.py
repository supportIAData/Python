from flask import Flask, render_template, redirect, url_for, abort, request, flash
from Data import users
from flask.config import Config
from utils import is_term_exist

app = Flask(__name__)

app.config.from_pyfile('config.py')

users = users.users

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', users=users)

@app.route('/user/<id>')
def user(id):
    return  render_template('user.html', user=user[id])

@app.route('/crud/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        email = request.form.get('email')
        if is_term_exist(email, users):
            flash('user already exist', 'error')

            return render_template('crud/add.html')
        
        users.append(request.form)

        flash('success add user', 'success')

        return redirect(url_for('home'))

    else:
        return render_template('crud/add.html')
    
