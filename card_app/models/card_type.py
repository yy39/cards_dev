from card_app.config.mysqlconnection import connectToMySQL


class CardType:
    def __init__(self, data):
        self.name = data['name']

    @staticmethod
    def get_all():
        query = 'SELECT * FROM card_types;'
        all_types = connectToMySQL('card_app_db_test').query_db(query)
        print(all_types)
        return all_types
