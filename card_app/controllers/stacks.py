import random
from card_app import app
from flask import render_template, redirect, request, session


@app.route('/stacks')
def stacks():
    return render_template('stacks.html')
