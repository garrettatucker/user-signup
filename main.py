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
    first_password_error = ""
    second_password_error = ""
    email_error = ""


    def filled_out(input):
        if input == "":
            return False
        else:   
            return True

    def no_spaces(input):
        if " " in input:
            return False
        else:
            return True

    def email_verify(input):
        if "@" and "." in input:
            return True
        else:
            return False

    def username_validation(name):
        if filled_out(name) == False or no_spaces(name) == False:
            username_error = "This field must be filled out"
            username = "" 
        elif len(name) < 3 or len(name) > 20:
                username_error = "This field must be between 3 and 20 characters"
                username = ""
        else:
            return first_password_validation(pass1)
    def first_password_validation(password):
        if filled_out(password) == False or no_spaces(password) == False:
            first_password_error = "This field must be filled out with no spaces"
            pass1 = ""
        elif len(password) < 3 or len(password) > 20:
                first_password_error = "This field must be between 3 and 20 characters"
                pass1 = ""
        else:
            return second_password_validation(pass2)
    def second_password_validation(verify):
        if filled_out(verify) == False or no_spaces(verify) == False:
            second_password_error = "This field must be filled out with no spaces"
            pass1 = ""
            pass2 = ""
        elif len(verify) < 3 or len(verify) > 20:
            second_password_error = "This field must be between 3 and 20 characters"
            pass1 = ""
            pass2 = ""
        else:
            return email_validation(email)
    def email_validation(address):
        if filled_out(address) == False or no_spaces(address) == False:
            email_error = "This field must be filled out with no spaces"
            email = ""
        elif len(address) < 3 or len(address) > 20:
                email_error = "This field must be between 3 and 20 characters"
                email = ""
        else:
           return welcome(username)
    def welcome(name):
        return "<h1>Welcome " + name + "!</h1>"

    return username_validation(username)

app.run()