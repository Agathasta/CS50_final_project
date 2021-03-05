import os

import sqlite3
import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Create a cursor to access the db
connection = sqlite3.connect("todos.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


@app.route("/")
@login_required
def index():
    now = datetime.datetime.now()
    dayname = now.strftime("%A").upper()
    date = now.strftime("%B %d, %Y").upper()
    return render_template("day.html", dayname=dayname, date=date)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("You must provide a username")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("You must provide a password")
            return render_template("login.html")

        # Query database for username & remember which user has logged in
        name = request.form.get("username")
        password = request.form.get("password")

        cursor.execute("SELECT * FROM users WHERE username = ?", (name,))
        row = cursor.fetchone()
        if row == None or not check_password_hash(row["hash"], password):
            flash("Invalid username and/or password")
            return render_template("login.html")

        session["user_id"] = row["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username and password were submitted, user doesn't exist, and same password was typed twice
        if not request.form.get("username"):
            flash("You must provide a username")
            return render_template("register.html")

        elif not request.form.get("password"):
            flash("You must provide a password")
            return render_template("register.html")
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        cursor.execute("SELECT * FROM users WHERE username = ?", (name,))
        row = cursor.fetchone()
        if row != None:
            flash("Username already exists")
            return render_template("register.html")            

        elif password != confirmation:
            flash("Passwords must match")
            return render_template("register.html")              

    	# Generate hash and add user to db
        hash = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                       (name, hash))
        connection.commit()

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
	"""Log user out"""

	# Forget any user_id
	session.clear()

    # Redirect user to login form
	return render_template("logout.html")

if __name__ == "__application__":
    app.run(debug=True)