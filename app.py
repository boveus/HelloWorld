from flask import Flask
import flask_login
login_manager = flask_login.LoginManager()

login_manager.init_app(app)

app = Flask(__name__)

users = {'foo@bar.tld': {'password': 'secret'}}

@app.route("/")
def hello():
    return "Hello World!"

