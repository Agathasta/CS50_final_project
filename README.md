****** TöDös ******
===================

CS50x Final Project
-------------------

For my final project I wanted to do a TODO list (I know, I know). I don't like any of the apps out there - ideally I would like a mixture of a calendar, a task manager and a simple list for not stricly scheduled todos like the [TeuxDeux](https://teuxdeux.com/) app. I'm going to start with the latter, I love its approach (if you like the idea check them out.)

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
    * to access fields by column name
    * selecting expects a tuple as value, so it needs parenthesis and a comma after the name (or square brackets and no comma)
    * selecting returns an object: select one row with fetchone() (if no row is found it returns None), and the value of a key (column) with _return row\['id']_

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
    This was hard. I had no idea where to start and in which direction to go. Right now I am grabbing the HTML input with Flask and inserting into the database (POST). For GET, Flask sends a JSON to JavaScript, and JS modifies the HTML.
