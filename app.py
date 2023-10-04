from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Import and register routes from routes.py
from routes import *

if __name__ == '__main__':
    app.run(debug=True)