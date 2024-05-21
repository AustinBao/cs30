from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import os
import datetime
from bson.objectid import ObjectId


# Different flask http methods: https://www.geeksforgeeks.org/flask-http-method/

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = './static/meme_imgs/'
app.secret_key = os.urandom(12)
client = MongoClient("mongodb+srv://austin:slimecheese123@memesite.qustpit.mongodb.net/?retryWrites=true&w=majority&appName=Memesite")
app.db = client.memesite

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class Meme:
    def __init__(self, image_name, name, description, year, source):
        self.image_name = image_name
        self.name = name
        self.description = description
        self.year = year
        self.source = source

    def save_to_db(self):
        meme_data = {
            'image_name': self.image_name,
            'name': self.name,
            'description': self.description,
            'year': self.year,
            'source': self.source,
            'user_id': session['user_id']
        }
        app.db.memes.insert_one(meme_data)

    def last_seen(self):
        current_year = datetime.date.today().year
        return current_year - self.year
    
    def update_in_db(self, meme_id):
        updated_meme = {
            'image_name': self.image_name,
            'name': self.name,
            'description': self.description,
            'year': self.year,
            'source': self.source 
        }
        # delete past image when edited
        old_meme = app.db.memes.find_one({'_id': ObjectId(meme_id)})
        if os.path.exists(f"/meme_imgs/{old_meme["image_name"]}"):
            os.remove(f"/meme_imgs/{old_meme["image_name"]}")
        
        app.db.memes.update_one({'_id': ObjectId(meme_id)}, {'$set': updated_meme})
        return "success" 


@app.route("/", methods=['GET', 'POST', 'PUT'])
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
                filename,
                request.form.get('memeName'),
                request.form.get('memeDescription'),
                request.form.get('memeYear'),
                request.form.get('memeSource')
            )
            meme.save_to_db()
            return redirect(url_for('home'))
        else:
            flash('No file part')
            return redirect(request.url)
        
    user_id = session['user_id']
    memes = [
        (
            meme["image_name"],
            meme["name"],
            meme["description"],
            meme["year"],
            meme["source"],
            meme["_id"]
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

# FLask takes the URL parameter (<meme_id>) and automatically passes it to the "delete_meme" function as the "meme_id" argument
@app.route('/delete_meme/<meme_id>', methods=['DELETE'])
def delete_meme(meme_id):
    success = app.db.memes.delete_one({'_id': ObjectId(meme_id)})
    if success:
        return jsonify({'message': 'Meme deleted successfully'}), 200
    else:
        return jsonify({'message': 'Meme not found'}), 404
    

@app.route('/edit_meme/<meme_id>', methods=['PUT'])
def edit_meme(meme_id):
    edit_image = request.files.get('editImage')
    edit_name = request.form.get('editName')
    edit_description = request.form.get('editDescription')
    edit_year = request.form.get('editYear')
    edit_source = request.form.get('editSource')

    # Handle file upload
    if edit_image:
        filename = edit_image.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        edit_image.save(filepath)

    meme = Meme(
        filename,
        edit_name,
        edit_description,
        edit_year,
        edit_source
    )

    meme.update_in_db(meme_id)

    return redirect(url_for('home'))    



if __name__ == '__main__':
    app.run()

 