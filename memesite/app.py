from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import os


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(12)
client = MongoClient("mongodb+srv://austin:slimecheese123@memesite.qustpit.mongodb.net/?retryWrites=true&w=majority&appName=Memesite")
app.db = client.memesite
 

@app.route("/")
def home():
    users = [
        (
            user["name"],
            user["email"],
            user["password"]
        )
        for user in app.db.users.find({})
    ]
    return render_template("home.html", users=users)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)

        app.db.users.insert_one({"name": name, "email": email, "password": hashed_password})
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        user = app.db.users.find_one({"name": name})
        
        if user and check_password_hash(user['password'], password):
            flash('Successfully logged in!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            flash('get better bud')
            
    return render_template('login.html')


if __name__ == '__main__':
    app.run()

