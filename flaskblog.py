from flask import Flask,render_template,url_for

app = Flask(__name__)

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

if __name__=='__main__':
	app.run(debug=True)