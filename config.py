import os

basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
DATABASE = '/tmp/drello.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
MONGODB_SETTINGS = {'DB': "Drello"}

