#from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/index.html')
def home():
	# print(query_all())
	return render_template('index.html')

@app.route('/')
def NewHome():
	return home()


# @app.route('/blog.html',methods=["GET","POST"])
# def blog():
# 	if request.method == "GET":
# 		return render_template("blog.html")
# 	else :
# 		username = request.form['username']
# 		event = request.form["event"]
# 		phonenumber = request.form["phonenumber"]
# 		add_event(username,event,phonenumber)
# 		return NewHome()
# @app.route('/about.html')
# def about():
# 	return render_template("about.html")














# @app.route('/login', methods=['POST'])
# def login():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return home()


# @app.route('/signup', methods=['POST'])
# def signup():
#     #check that username isn't already taken
#     user = get_user(request.form['username'])
#     if user == None:
#         add_user(request.form['username'],request.form['password'])
#     return home()


# @app.route('/logged-in')
# def logged_in():
#     return render_template('logged.html')


# @app.route('/logout')
# def logout():
#     login_session['name'] = None
#     login_session['logged_in'] = False
#     return home()



if __name__ == '__main__':
	app.run(debug=True)
