from flask import Flask
from flask_sqlalchemy import SQLAlchemy,


app = Flask(__name__)
app.config['SECRET_KEY'] = '7cd18ff261d5dbe21f54af94fb3a78cc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes