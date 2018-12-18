from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect("/signup")
@app.route("/signup")
def DisplaySignup():
    return render_template('MainForm.html')
@app.route("/signup", methods= ['POST'])
def ValidateSignup():
    username = cgi.escape(
        request.form['username'])
    password = cgi.escape(
        request.form['password'])
    Confirmpass = cgi.escape(
        request.form['verify'])
    email = cgi.escape(
        request.form['email'])
    username_new = ""
    password_new = ""
    Confirmpass_new = ""
    email_new = ""

    if  username == "":
        username_new = "That username is invalid"
    elif len(username) > 15 or len(username) < 3:
        username_new = "That username is invalid"
    if password == "":
        password_new = "That password is invalid"
    elif len(password) > 15 or len(password) < 3:
        password_new = "That not a valid password"
    if Confirmpass == "":
        Confirmpass_new = "The password does not match"
    elif not password == Confirmpass:
        Confirmpass_new = "The password does not match"
    
    if len(email) > 0:
        if email.count("@") < 1:
            email_new = "Invalid Email"
        elif email.count(".") < 1:
            email_new = "Invalid Email"
        elif email.count(" ") > 0:
            email_new = "Invalid Email"
        elif len(email) > 15 or len(email) < 3:
            email_new = "Invalid Email"
    
    if not username_new and not password_new and not Confirmpass_new and not email_new:
        return redirect('/welcome?username= {0}'.format(username))
        #return "<h1> Hello "+ username +"! </h1>"
    else:
        return render_template('MainForm.html', 
            username= username, username_new= username_new, 
            password_new= password_new, Confirmpass_new= Confirmpass_new,
            email= email, email_new= email_new)


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username= username)



app.run()