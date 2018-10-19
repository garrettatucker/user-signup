from flask import Flask, request
from index import form
from welcome import welcome
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["POST"])
def check_info():
    username = request.form["username"]
    pass1 = request.form["pass1"]
    pass2 = request.form["pass2"]
    email = request.form["email"]

    if len(username) < 3 or len(username) > 25:
        return "username needs to be between 3 and 25 characters long."
    elif pass2 != pass1:
        return "passwords must match!"
    elif len(pass1) and len(pass2) < 6 or len(pass1) and len(pass2) > 25:
        return "passwords must be between 6 and 25 characters long."
    else:
        welcome(username)

@app.route("/")
def index():
    return form
app.run()