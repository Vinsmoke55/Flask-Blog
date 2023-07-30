from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='4e46bf8c58b1c5be82332c606adf2d4d'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True,nullable=False)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
	password=db.Column(db.String(60),nullable=False)
	posts=db.relationship('Post',backref='author',lazy=True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}'),"

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True,nullable=False)
	title=db.Column(db.String(100),nullable=False)
	date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	content=db.Column(db.Text,nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

	def __repr__(self):
		return f"Post('{self.title}',{self.date_posted}'),"



posts=[
{
	'author':'ayush',
	'title':'first blog post',
	'content':'i am learning flask',
	'date':'July 28,2023'
},
{
	'author':'Ariana',
	'title':'second blog post',
	'content':'i am learning django',
	'date':'July 27,2023'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account have been created for {form.username.data}",'success')
		return redirect(url_for('home'))
	return render_template('register.html',title='register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data=="neupaneayush3@gmail.com" and form.password.data=="password":
			flash("You are logged in ",'success')
			return redirect(url_for('home'))
		else:
			flash("login failed",'danger')
	return render_template('login.html',title='login',form=form)

if __name__=='__main__':
	app.run(debug=True)