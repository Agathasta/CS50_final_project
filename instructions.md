# ****** INSTRUCTIONS ******

Activate venv:
  $ . venv/bin/activate

To create requirements document, from within the environment:
  $ pip freeze > requirements.txt

  ------------------------------------------------

To create a v-env, from within the project folder,
  $ python3 -m venv venv

To use this document to install dependencies, from within a v-env:
  $ pip install -r requirements.txt

  ------------------------------------------------

To run flask, from within the environment
  export FLASK_APP=application.py
  export FLASK_ENV=development
  flask run

## Steps to connect app -> db

_import sqlite3

* make a connection application -> database
_connection = sqlite3.connect("todos.db")_
* to access fields by column name
_connection.row\_factory = sqlite3.Row_
* cursor to access the actual db
_cursor = connection.cursor()_
* when selecting, it expects a tuple as value, so it needs parenthesis and a comma after the name (or square brackets and no comma)
_cursor.execute('SELECT * FROM users WHERE user = ?', (user,))_
_cursor.execute('SELECT * FROM users WHERE user = ?', \[user])_
* select returns an object. To select one row, use fetchone(); if no row is found it returns None
_row = cursor.fetchone()_
* return the value of a key (column) in one row (so, if more rows, iterate over them)
_return row\['id']_
