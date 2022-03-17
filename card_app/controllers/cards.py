from card_app import app
from flask import render_template, redirect, request, session
from card_app.models.card import Card
from card_app.config.mysqlconnection import connectToMySQL, queryMySQL


@app.route('/')
def index():
    if session:
        print(session)
    return render_template('index.html')


@app.route('/cards/new')
def new_card():
    return render_template('new_card.html')


@app.route('/cards/create', methods=['POST'])
def create_card():
    Card.create_card(request.form)
    return redirect('/cards')


@app.route('/cards')
def show_cards():
    cards = connectToMySQL("card_app_db_test").query_db("SELECT * FROM cards;")
    return render_template('cards.html', cards=cards)


@app.route('/cards/show/<int:id>')
def show_card(id):
    card = Card.get_card({"id": id})
    return render_template('show_card.html', card=card)
