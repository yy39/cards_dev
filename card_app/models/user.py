import re
from card_app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.username = data['username']
        self.display_name = data['display_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (username, display_name, email, password) VALUES (%(username)s, %(display_name)s, %(email)s, %(password)s);'
        user = connectToMySQL('card_app_db_test').query_db(query, data)
        flash('User successfully created')
        return user

    @classmethod
    def get(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        user = connectToMySQL('card_app_db_test').query_db(query, data)
        if user:
            return cls(user[0])

    @staticmethod
    def get_all():
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL('card_app_db_test').query_db(query)
        if all_users:
            return all_users

    @staticmethod
    def validate(user):
        is_valid = True
        # username validation
        if len(user['username']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        # display_name validat8on
        if len(user['display_name']) < 3:
            flash('Display name must be at least 3 characters.')
            is_valid = False
        # email validation
        if len(user['email']) < 5:
            flash('Email must be at least 5 characters.')
            is_valid = False
        elif len(user['email']) >= 255:
            flash('Email must be less than 255 characters.')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address')
            is_valid = False
        # password validation
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        # unique validation
        if is_valid:
            query = "SELECT username, email FROM users;"
            uniques = connectToMySQL('card_app_db_test').query_db(query)
            print(uniques)
        return is_valid
