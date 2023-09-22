import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

from apps.models import *
from apps.todo import todoApi

app = Flask(__name__)
load_dotenv()

# configure flask application
debug_mode = os.getenv("DEBUG", True)
secret_key = os.getenv("SECRET_KEY")
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
track_db_modifications = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_db_modifications

# configure migrations
db.init_app(app)

migrate = Migrate(app, db)

CORS(app)

app.register_blueprint(todoApi)

if __name__ == '__main__':
    # run flask server
    app.run(host='0.0.0.0', port=5000)
