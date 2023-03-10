# -----------------------
# imports os libraries so the program can work with the functions
# of the software its running through
# -----------------------
import os
# -----------------------
# imports the FLask class from the flask library
# (imports flask into the document)
# -----------------------
from flask import Flask

# -----------------------
# Creates and instance of a flask app.
# at this point, the app doesnt do anything though
# -----------------------
app = Flask(__name__)


# -----------------------
# creates a route the app can launch from,
# and also what it will do once it has beeen succesfully run
# -----------------------
@app.route("/")
# -----------------------
# here, it's just going to print "hello world" on an index page
# -----------------------
def index():
    return "Hello, world"


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
