from card_app import app
from flask import render_template, redirect, request, session
from card_app.models.card import Card
from card_app.models.card_type import CardType
from card_app.config.mysqlconnection import connectToMySQL, queryMySQL


@app.route('/')
def index():
    error = None
    if session:
        print(session)
    return render_template('index.html', error=error)


@app.route('/cards/new')
def new_card():
    all_types = CardType.get_all()
    return render_template('new_card.html', types=all_types)


@app.route('/cards/create', methods=['POST'])
def create_card():
    if not Card.validate_card(request.form):
        return redirect('/cards/new')
    Card.create_card(request.form)
    return redirect('/cards')


@app.route('/cards')
def show_cards():
    cards = Card.get_all()
    return render_template('cards.html', cards=cards)


@app.route('/cards/<int:id>')
def show_card(id):
    card = Card.get_card({'id': id})
    return render_template('show_card.html', card=card)
