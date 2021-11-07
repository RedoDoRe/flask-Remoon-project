from flask import (Flask, 
				request,
				 render_template,
				 url_for ,
				 redirect)


app = Flask(__name__)





@app.route('/home')
def home():
	return render_template('layout.html')



@app.route('/',methods=['GET','POST'])
@app.route('/signin',methods=['GET','POST'])
def signin():
	message =''
	if request.method =='POST':
		email = request.form['email']
		password = request.form['password']
		if  email == 'admin' and password =='admin':		
			return redirect(url_for('home'))
		else:
			message= 'Sai tên tài khoản hoặc mật khẩu'
			
	return render_template('signin.html',title ='sign in',message=message)

@app.route('/signup')
def signup():
	return render_template('signup.html',title ='sign up')


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 9999, debug = True)