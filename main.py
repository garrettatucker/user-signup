from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")




@app.route("/", methods=["POST"])
def check_info():
    username = request.form["username"]
    pass1 = request.form["pass1"]
    pass2 = request.form["pass2"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    password_match_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20:
        username_error = "usernames cannot be blank and must be between 3 and 20 characters"
        username = ""
    elif " " in username:
        username_error = "usernames cannot contain any spaces"
        username = ""
    if len(pass1) < 3 or len(pass1) > 20 or " " in pass1:
        password_error = "passwords cannot be blank and must be between 3 and 20 characters"
        pass1 = ""
    elif pass2 != pass1:
        password_error = "passwords must match"
        pass2 = ""
    if len(email) != 0 and len(email) < 3 or len(email) > 20:
        email_error = "emails need to be between 3 and 20 characters in length"
        email = ""
    elif " " in email or "@" not in email and "." not in email:
        email_error = "email is not formatted correctly"
        email = ""
    if not username_error and not password_error and not email_error:
        return "<h1>Welcome " + username + "!</h1>"
    else:
        return render_template("form.html" , username_error = username_error , password_error = password_error, password_match_error = password_match_error, email_error = email_error, username = username, pass1 = pass1, pass2 = pass2, email = email)
def welcome(name):
    return "<h1>Welcome " + name + "!</h1>"

app.run()