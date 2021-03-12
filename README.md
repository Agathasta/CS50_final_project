# One Place
Centralize ToDos - Appointments - Jobs - Birthdays - Lists  
v.1.0
## CS50x Final Project

[Video Demo](https://youtu.be/2DKeyi2YDGA)

For my final project I wanted to do a TODO list (I know, I know). I don't like any of the apps out there - ideally I would like a mixture of a calendar, a task manager and a simple list for not stricly scheduled todos like the [TeuxDeux](https://teuxdeux.com/) app. I'm going to start with the latter, I love its approach (and if you like the idea do check them out.)

1. INSTALL DEPENDENCIES  
    I thought I would just more or less copy the Finance problem set 9 implementation of register and login and concentrate on the actual ToDos. Ha! Since I'm not using the CS50 IDE, it took me hours to find out what I needed and install it (sigh).

    What I learned:
    * why and how to create a virtual environment
    * how to install the needed libraries
    * why and how to create a _requirements.txt_ document

2. REGISTER and LOGIN  
    The next hurdle was to actually connect the database with the application and interact with it. I think it works now, with all the error possibilities taken care of.

    What I learned:
    * to make a connection application -> database
    * select expects a tuple as value, so it needs parenthesis and a comma after the name (or square brackets and no comma)
    * select returns an object: select one row with fetchone() (if no row is found it returns None)
    * to access fields by column name use first _connection.row\_factory = sqlite3.Row_

3. CSS  
    Next I started fighting with Bootstrap, starting to give what I had a look.

    What I learned:
    * To make the navbar fixed and get the rest to behave normally (adding a top padding to the body)
    * To get a background image and to position text and buttons on top of it where I want them to be.
    * To justify and align content and forms

4. FLASH  
    The substitution of error pages for flashed messages went surprisingly fast and smooth. I changed it because I didn't think getting a different error page for every error was a good user experience. The flashed messages look good and do warn the user enough of what the problem is.

    What I learned:
    * To check if conditions are met, and if they aren't, stay on the same page and flash a warning.

    Status: at this point I am good 10 hours into the project, including this documentation.

5. SQL connected to JS through Flask  
    This was hard. I had no idea where to start and in which direction to go. Right now I am grabbing the HTML input with Flask and inserting into the database (POST). For GET, Flask sends a JSON to JavaScript, and JS modifies the HTML creating a list of ToDos.

6. START FROM ZERO!!!  
    This was getting more and more complicated. I had the following working: a display of ToDos and the possibility of adding ToDos (see above). I was deleting from the DB with GET, sending the ToDo to be deleted through an URL, and then having JS display all ToDos again. The whole thing worked (and looked good) but it was getting monstruous, and I was stumped trying to edit or cross out ToDos...
    So I googled again, and found a wonderful simple Flask ToDo app that gave me the push to rethink everything (well, obvioulsly not everything, but everything I have tried in the past two days).

7. Installing SQLAlquemy  
    And the first thing I did was swallow my pride at having my raw SQL queries working and give SQLALchemy a chance. I have spent the morning reading documentation, and have adapted my register and login queries in about 5 minutes. I tell myself than knowing what a connection and a cursor is will make my future brighter....... Sigh.

    What I learned:
    * What an ORM is (kind of, at least)
    * To create a db, tables, relationships
    * To query said db
    * To be awed at the clarity of the results. Goodby tuples!!!

    Status: at this point I am over 24 hours into the project... Lots of time spent trying things out, googling, making tiny steps, retracing them. But hey, I am feeling confident again :)

8. Reduce expectations and call it a day (for now)  
    Well... I must be at around 40-45 hours and I am frustrated. I know frustration is part of it, but I am missing way too much knowledge: I started this with no clue of Python or Flask or SQLAlchemy or JS, and I have decided that I am going to leave it at this for the moment.  
    I spent ages trying to change the day for which I was seeing the ToDos, I tried the HTML date input, but Flask wouldn't recognize the input (None was its stubborn answer), I tried setting the default date with JS, sending the input with jQuery AJAX so as not to reload the page, I tried modals... I don't even remember the millon of things I tried. I think (I hope) it's just because I'm blocked and need a pause. I feel like when you spin around too often and then cannot even make the smallest step straight.  
  
    I do like what I have done until now, I still like my original app idea, and I have learned a ton! :)  

9. DATE CHANGE
    Of course, a couple of hours after submitting here I am, happily overcoming those alpine heights I was just whining about (eyeroll).
    The  user can now change the date, and the appropiate ToDos will show and work as expected, ToDos can be added, checked and deleted. Missing only the beauty details, like deciding what to do with the input field. I cannot believe  how blocked I was :/  

    What I learned:
    * Optional arguments to URLs are possible.
    * A session can be used for things that need to be moved around, like the date.
    * Converting strings to dates and dates to strings, although I suspect I managed to make that work by sheer luck.

THANKS TO:  

* [CS50x](https://cs50.harvard.edu/college/2021/spring/)
* [PythonEngineer](https://www.python-engineer.com/posts/flask-todo-app/)
* [Rapid Python](https://rapidpython.com/build-application-using-python-flask-heroku-tailwind/)
* [opensource](https://opensource.com/article/18/4/flask)
* [w3schools](https://www.w3schools.com)  

And all the people out there writing documentation, sharing knowledge and answering questions!!!
