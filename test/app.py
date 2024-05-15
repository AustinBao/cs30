import os
from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)
MONGO_URI = "mongodb+srv://austin:slimecheese123@memesite.qustpit.mongodb.net/?retryWrites=true&w=majority&appName=Memesite"
client = MongoClient(MONGO_URI)
app.db = client.memesite


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        app.db.users.insert_one({"name": name, "email": email, "password": password})

    users = [
        (
            user["name"],
            user["email"],
            user["password"]
        )
        for user in app.db.users.find({})
    ]
 
    return render_template("home.html", users=users)




# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://austin:slimecheese123@memesite.qustpit.mongodb.net/?retryWrites=true&w=majority&appName=Memesite"

# client = MongoClient(uri, server_api=ServerApi('1'))

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)