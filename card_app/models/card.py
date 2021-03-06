from card_app.config.mysqlconnection import connectToMySQL, queryMySQL
from flask import flash


class Card:
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.value = data['value']

    @classmethod
    def create_card(cls, data):
        query = 'INSERT INTO cards (type, name, value) VALUES (%(type)s, %(name)s, %(value)s);'
        flash('Card successfully created')
        return queryMySQL(query, data)

    @classmethod
    def get_card(cls, data):
        query = 'SELECT * FROM cards WHERE id = %(id)s;'
        card = queryMySQL(query, data)
        if card:
            return cls(card[0])

    @staticmethod
    def get_all():
        query = 'SELECT cards.id, cards.name, card_types.name as type, value from cards JOIN card_types ON cards.type = card_types.id;'
        all_cards = connectToMySQL("card_app_db_test").query_db(query)
        print(all_cards)
        return all_cards

    @staticmethod
    def validate_card(card):
        is_valid = True
        if len(card['name']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        # type shouldn't need validation but we will check it anyways later
        # to do: add validation for type
        if len(card['value']) < 3:
            flash('Value must be at least 3 characters.')
            is_valid = False
        return is_valid
