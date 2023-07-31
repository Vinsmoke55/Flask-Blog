from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.form import RegistrationForm,LoginForm
from flaskblog.models import User,Post


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
