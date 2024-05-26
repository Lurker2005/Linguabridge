import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

# Assuming this function connects to the database and returns user data
from connect import *

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key
app.static_folder = "static"
app.config['UPLOAD_FOLDER'] = 'uploads'  # Set the upload folder

@app.route("/", methods=["GET", "POST"])
def login_route():
    if request.method == "POST":
        user = request.form["username"]
        pas = request.form.get('password')
        # Call your login function to validate credentials
        result = login("localhost", "root", "Robotics26!", "world")
        for i in result:
            if user in i and pas in i:
                session['user_id'] = user  # Set user_id in session
                return redirect(url_for('home'))
        flash("Wrong username or password.", "danger")
    
    param = request.args.get('param')
    if param == "signup":
        return redirect(url_for('signup'))
    
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        na = request.form["fullname"]
        us = request.form["username"]
        ea = request.form["email"]
        ps = request.form["password"]
        sign("localhost", "root", "Robotics26!", "world", na, us, ea, ps)
        flash("Sign up successful! Please log in.", "success")
        return redirect(url_for('login_route'))

    return render_template("sign.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    user_id = session.get('user_id', None)  # Retrieve user_id from session
    if user_id is None:
        return redirect(url_for('login_route'))
    
    param = request.args.get('param')
    langs = request.args.get('langs')

    if param == "help":
        return redirect(url_for('help'))

    return render_template('home.html', user_id=user_id)

@app.route("/help", methods=["GET", "POST"])
def help():
    param = request.args.get('param')
    if param == "home":
        return redirect(url_for('home'))
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True)
