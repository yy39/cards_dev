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
        return queryMySQL(query, data)

    @classmethod
    def get_card(cls, data):
        query = 'SELECT * FROM cards WHERE id = %(id)s;'
        card = queryMySQL(query, data)
        if card:
            return cls(card[0])

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
