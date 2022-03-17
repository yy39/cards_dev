from card_app.config.mysqlconnection import connectToMySQL, queryMySQL


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
