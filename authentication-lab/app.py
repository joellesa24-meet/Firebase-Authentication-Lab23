from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config={
 "apiKey": "AIzaSyA1Am-vzXsXOvm6njjQCIf65ogLmsx5l8A",
  "authDomain": "the-project-b30da.firebaseapp.com",
  "projectId": "the-project-b30da",
  "storageBucket": "the-project-b30da.appspot.com",
  "messagingSenderId": "131076584651",
  "appId": "1:131076584651:web:d230d1d31241dc18a8974e",
  "measurementId": "G-1JZ2JN6KJR",
   "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password=request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
              error = "Authentication failed"
    return render_template("signup.html")   




@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")






if __name__ == '__main__':
    app.run(debug=True)