from collections import namedtuple

import time

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))
    time.sleep(5)

    return redirect(url_for('main'))


@app.route('/err', methods=['POST'])
def err():
    raise Exception('ops')
