# import os

# import sqlite3
from datetime import datetime, date
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application and db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///remember.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    todos = db.relationship('Todos', backref='user', lazy=True)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False,
        default=datetime.now().date())
    done = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)


# Ensure templates are auto-reloaded *** FROM CS50 ***
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies) *** FROM CS50 ***
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

now = datetime.now().strftime("%Y-%m-%d")

@app.route("/")
@app.route("/<date>")
@login_required
def home(date=now):
    """Show homepage"""

    user_id = session.get("user_id")
    date = datetime.strptime(date, '%Y-%m-%d').date()
    session["date"]=date

    if date == now:
        todos = Todos.query.filter_by(user_id=user_id, done=False).all()
        for todo in todos:
            if todo.date < date:
                todo.date = date
        db.session.commit()

    todo_list = Todos.query.filter_by(user_id=user_id, date=date).order_by(Todos.done).all()
    
    return render_template("home.html", todo_list=todo_list, date=date)
        

@app.route("/add", methods=["POST"])
@login_required
def add():
    """Add ToDo"""

    # Get data to put in the new ToDo
    todo = request.form.get("todo")
    date = session.get("date")
    user_id = session.get("user_id")

    # Add the new ToDo
    new_todo = Todos(todo=todo, date=date, done=False, user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("home", date=date))


@app.route("/delete/<int:todo_id>/<date>")
@login_required
def delete(todo_id, date):
    """Delete todo"""

    todo = Todos.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("home", date=date))


@app.route("/check/<int:todo_id>/<date>")
@login_required
def check(todo_id, date):
    """Check/Uncheck ToDo"""

    todo = Todos.query.filter_by(id=todo_id).first()
    todo.done = not todo.done
    db.session.commit()

    return redirect(url_for("home", date=date))


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
        user = Users.query.filter_by(username=name).first()
        if user == None or not check_password_hash(user.password, password):
            flash("Invalid username and/or password")
            return render_template("login.html")
        
        # Remember which user has logged in
        session["user_id"] = user.id

        # Redirect user to home page
        return redirect(url_for("home"))

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
        user = Users.query.filter_by(username=name).first()
        if user != None:
            flash("Username already exists")
            return render_template("register.html")            

    	# Generate hash and add user to db
        password = generate_password_hash(password)

        new_user = Users(username=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Automatically log in
        user = Users.query.filter_by(username=name).first()
        session["user_id"] = user.id

        return redirect(url_for("home"))

    else:
        return render_template("register.html")


@app.route("/welcome")
def logout():
	"""Greet logged out user"""

	# Forget any user_id  *** FROM CS50 ***
	session.clear()

    # Redirect user to login form
	return render_template("logout.html")


if __name__ == "__application__":
    db.create_all()
    app.run(debug=True)
