import card

class Stack:
    def __init__(self, name='Placeholder Text', size=0):
        self.name = name
        self.content = {0: Card('Placeholder Text', 0)}
        self.size = size