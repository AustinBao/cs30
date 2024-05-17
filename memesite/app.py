from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import os


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = './static/meme_imgs/'
app.secret_key = os.urandom(12)
client = MongoClient("mongodb+srv://austin:slimecheese123@memesite.qustpit.mongodb.net/?retryWrites=true&w=majority&appName=Memesite")
app.db = client.memesite

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class Meme:
    def __init__(self, image_path, name, description, year, source):
        self.image_path = image_path
        self.name = name
        self.description = description
        self.year = year
        self.source = source

    def save_to_db(self):
        meme_data = {
            'image_path': self.image_path,
            'name': self.name,
            'description': self.description,
            'year': self.year,
            'source': self.source,
            'user_id': session['user_id']
        }
        app.db.memes.insert_one(meme_data)


@app.route("/", methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        img_file = request.files.get("memeImage")
        if img_file:
            filename = img_file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(filepath)

            meme = Meme(
                image_path=filename,
                name=request.form.get('memeName'),
                description=request.form.get('memeDescription'),
                year=request.form.get('memeYear'),
                source=request.form.get('memeSource')
            )
            meme.save_to_db()
            return redirect(url_for('home'))
        else:
            flash('No file part')
            return redirect(request.url)
        
    user_id = session['user_id']
    memes = [
        (
            meme["image_path"],
            meme["name"],
            meme["description"],
            meme["year"],
            meme["source"]
        )
        for meme in app.db.memes.find({"user_id": user_id})
    ]
    return render_template("home.html", memes=memes)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)

        app.db.users.insert_one({"username": username, "email": email, "password": hashed_password})
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        check_user = app.db.users.find_one({"username": username})

        if check_user and check_password_hash(check_user['password'], password):
            flash('Successfully logged in!')
            session['user_id'] = str(check_user['_id'])
            session['user_name'] = check_user['username']
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            flash('reset password')
            
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()

