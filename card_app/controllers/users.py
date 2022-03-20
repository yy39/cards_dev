from card_app import app
from flask import render_template, redirect, request, session
from card_app.models.user import User


@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users=users)


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/create', methods=['POST'])
def create_user():
    if not User.validate(request.form):
        return redirect('/users/new')
    User.create(request.form)
    return redirect('/users')


@app.route('/login')
def login_page():
    return render_template('login.html')
