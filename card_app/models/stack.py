import card
from card_app.config.mysqlconnection import queryMySQL


class Stack:
    def __init__(self, data):
        self.name = data['name']
        self.cards = []
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']


@classmethod
def get_size():
    pass


@classmethod
def get_cards():
    pass


@classmethod
def create(cls, data):
    query = 'INSERT INTO stacks (name, cards) VALUES (%(name)s, %(cards)s)'
    stack = connectToMySQL('dogs_db').query_db(query, data)
    return stack


'''
    def show_card_at(self, position):
        if position in self.content:
            print(
                f'Showing Card: {self.content[position].name} from Stack: {self.name}')
            print(f'Position: {position}')
            self.content[position].show_card()
            return self

    def show_all_cards(self):
        print(f'\nShowing all cards from Stack: {self.name}')
        for i in range(self.size):
            self.show_card_at(i)
        return self

    def add_card(self, new_card):
        self.content[self.size] = new_card
        self.size += 1
        print('New Card added.')
        return self

    def top_card(self):
        print('Top Card')
        return self.content[len(self.content) - 1]

    def random_card(self):
        random_card_position = random.randrange(len(self.content))
        print()
        return self

'''
