__author__ = 'Mitu'


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)



from conversationAI.comment.views import comment_posts
from conversationAI.core.views import core


# Register the apps
app.register_blueprint(core)
app.register_blueprint(comment_posts)



