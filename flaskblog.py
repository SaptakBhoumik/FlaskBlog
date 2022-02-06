# 16:14
from datetime import datetime
from distutils.log import debug
from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from forms import registrationform, Loginform

app = Flask(__name__)

app.config["SECRET_KEY"] = '5mLwDAO8umfBU3AYpIGsV2YlF74o0airrXZfNXfgr9J2duPtZE3mo5fTgYdd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="author", lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    def __init__(self):
        self.id = db.Column(db.Integer, primary_key=True)
        self.title = db.Column(db.String(100), nullable=False)
        self.date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        self.content = db.Column(db.Text, nullable=False)
        self.user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        "author": "max tennyson",
        "title": "blog post 1",
        "content": "blueprints of the omnitrix spread through the entire universe, the entire multiverse at danger",
        "date_posted": "2 Feb, 2022"
    },
    {
        "author": "Sherlock, a great thought to be dead detective",
        "title": "blog post 2",
        "content": "Rohit Ghosh caught to be stealing doughnuts from dunkin doughnuts, fined for $2000",
        "date_posted": "3 Feb, 2022"
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for('hello_world'))
    return render_template("register.html", title='register', form=form)

@app.route("/login", methods=['POST','GET'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash('you have been logged in', "success")
            return redirect(url_for('hello_world'))
        else:
            flash("unsuccesful login pls check username and password", "danger")

    return render_template("login.html", title='login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
