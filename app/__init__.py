from flask import Flask
from config import Config
import os

# app = Flask(__name__, static_url_path='/../static')
app = Flask(__name__, static_url_path="/static", static_folder='static')
# app._static_folder = os.path.abspath("../static")
app.config['SECRET_KEY'] = 'laboratorium'

from app import routes