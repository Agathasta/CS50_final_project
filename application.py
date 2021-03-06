import os

import sqlite3
import datetime
from flask import Flask, flash, json, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded *** FROM CS50 ***
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies) *** FROM CS50 ***
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show homepage"""

    user = session.get("user_id")

    # Get current date
    now = datetime.datetime.now()
    dayname = now.strftime("%A").upper()
    date = now.strftime("%B %d, %Y").upper()

    if request.method == "POST":

        todo = request.form.get("todo")

        # Ensure a ToDo was written
        if not todo:
            flash("What do you have tö dö?")
            return redirect("/")

        with sqlite3.connect("todos.db") as conn:
            conn.execute("INSERT INTO todos (user_id, todo, status, date) VALUES(?, ?, ?, ?)",
                       (user, todo, "Not done", now))
        return redirect("/")

    else:
        with sqlite3.connect("todos.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todos WHERE user_id = ?", (user,))
            rows = cursor.fetchall()
            todos = json.dumps( [dict(row) for row in rows] )

        return render_template("day.html", user=user, dayname=dayname, date=date, todos=todos)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id  *** FROM CS50 ***
    session.clear()

    if request.method == "POST":

        name = request.form.get("username")
        password = request.form.get("password")

        # Ensure username and password are submitted
        if not name or not password:
            flash("You must provide a username and a password")
            return render_template("login.html")

        # Query database for existing username & matching password
        with sqlite3.connect("todos.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (name,))
            row = cursor.fetchone()
            if row == None or not check_password_hash(row["hash"], password):
                flash("Invalid username and/or password")
                return render_template("login.html")
        
        # Remember which user has logged in
        session["user_id"] = row["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        name = request.form.get("username")
        password = request.form.get("password")

        # Ensure username and password were submitted, user doesn't exist, and same password was typed twice
        if not name:
            flash("You must provide a valid username")
            return render_template("register.html")

        elif not password:
            flash("You must provide a valid password")
            return render_template("register.html")

        elif password != request.form.get("confirmation"):
                flash("Passwords must match")
                return render_template("register.html")

        # Query database for existing username
        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (name,))
            row = cursor.fetchone()
            if row != None:
                flash("Username already exists")
                return render_template("register.html")            

    	# Generate hash and add user to db
        hash = generate_password_hash(password)
        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (name, hash))
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
	"""Log user out"""

	# Forget any user_id  *** FROM CS50 ***
	session.clear()

    # Redirect user to login form
	return render_template("logout.html")

if __name__ == "__application__":
    app.run(debug=True)
