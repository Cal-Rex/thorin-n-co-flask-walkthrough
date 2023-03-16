# -----------------------
# imports os libraries so the program can work with the functions
# of the software its running through
# -----------------------
import os
# -----------------------
# imports json library
# -----------------------
import json
# -----------------------
# imports the FLask class from the flask library
# (imports flask into the document)
# -----------------------
# render_template:
# render_template(filepath) function can be used to select files from directory
# -----------------------
# request
# library in flask, helps manage form data and form methods
# -----------------------
# flash
# library that contains functionality to present flashed messages to the user,
# such as a "thank you for fubmitting this form" message
# flash needs a secret key to work
# -----------------------
from flask import Flask, render_template, request, flash
# -----------------------
# secret key linked up to python file by using if statement
# if the following filepath exists and can be accessed
# -----------------------
# import the env.py, short for "environment" or "environ"
# hide sensetive data and environment variables in there that
# should not be posted publicly
# if statement is used here to determine wether
# or not to use key
# depending on whether the key exists
if os.path.exists("env.py"):
    import env

# -----------------------
# Creates and instance of a flask app.
# at this point, the app doesnt do anything though
# -----------------------
app = Flask(__name__)
# -----------------------
# creates an instance of the secret key for flash functions
# -----------------------
app.secret_key = os.environ.get("SECRET_KEY")


# -----------------------
# creates a route the app can launch from,
# and also what it will do once it has beeen succesfully run
# -----------------------
@app.route("/")
# -----------------------
# here, it's just going to print "hello world" on an index page
# will print default strings in HTML
# -----------------------
def index():
    # -----------------------
    # will print default strings in HTML
    # -----------------------
    # return "<h1>Hello, world</h1>"
    # -----------------------
    # will "render" the following page inside the templates folder & return it
    # -----------------------
    return render_template("index.html")


# -----------------------
#  About section will now access the
# company.json file and display it's contents
# -----------------------
@app.route("/about")
def about():
    # an empty variable is created to store the data
    # unpacked/taken from the json file
    data = []
    # This statement could be read in english as
    # "with the file under filepath data/company.json,
    #  open it in a 'read-only' context, and label it as 'json_data'"
    # ["r" indicates file to be opened as "read-only"]
    with open("data/company.json", "r") as json_data:
        # the empty data variable now houses the company.json contents,
        # and with the json.load(variable) command loads that contents as
        # JSON (JavaScript Object Notation)
        data = json.load(json_data)
    # in the return statement, the now-filled "data" variable
    # is now assigned to the variable of "company",
    # which is called on the about page using flask notation
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    dwarf = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                dwarf = obj
    # in the_render template statement below,
    # the second argument contains "member=dwarf",
    # the "member" is referring to the pre-established variable
    # stated within member.html
    # "dwarf", refers to the object established at the top of the function
    # where the for loop has parsed data into
    return render_template("member.html", member=dwarf)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # if statement is checking if a request made by a form is a post method
    if request.method == "POST":
        # string will be flashed to the page upon successful reload
        # after submission
        flash(
            "Thanks {}! We have got your message!".format(
                request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# -----------------------
# __main__ is the default function that runs first in a python file.
# if it is not otherwise specified, it will be the first thing to run
# -----------------------
if __name__ == "__main__":
    # -----------------------
    # app.run runs the specified function, the elements in the brackets
    # indicate where it is going to run
    # -----------------------
    app.run(
        # -----------------------
        # os called, targets an environment and gets its data so it knows
        # where to deploy/display returned values of app function
        # -----------------------
        host=os.environ.get("IP", "0.0.0.0"),
        # -----------------------
        # determines what port it will run out of
        # -----------------------
        port=int(os.environ.get("PORT", "5000")),
        # -----------------------
        # only to be set as True when debugging - working on code,
        # otherwise it is a SECURITY RISK
        # -----------------------
        debug=True)
