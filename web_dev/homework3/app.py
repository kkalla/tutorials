"""Todo List web app
1. need pages
    * Terms of Use
    * Privacy
    * About Us
    All of these are gonna be placed in footer

2. Add Signup and Signin process + logout
3. login -> user specific dashboard (using redis)
4. create a new list or click on any existing list
5. There are tasks in the list. Need to add functions below
    * name/rename list and tasks
    * add tasks
    * remove tasks
    * "check off"
    * delete the entire list

For now in homework3
1. make a list of all the individual routes and pages
2. Choose the database. -> PostgreSQL
3. Design the database schema. export schema / table-structure

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')


@app.route('/signin', methods=["GET"])
def signin():
    return render_template('signin.html')


@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")


@app.route('/terms', methods=["GET"])
def terms():
    return render_template("terms.html")


@app.route('/privacy', methods=["GET"])
def privacy():
    return render_template("privacy.html")


if __name__ == "__main__":
    app.run()
