from flask import Flask
from flask.ext.mongoengine import MongoEngine



app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)


from app.views import *
from app.models import *


