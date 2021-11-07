from flask import Flask, request, render_template,url_for


app = Flask(__name__)

@app.route('/home')
def home():
	return '<p>Hello Word</p>'

@app.route('/')
@app.route('/signin')
def login():
	return render_template('login.html')

@app.route('/signup')
def register():
	return render_template('register.html')


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 9999, debug = True)