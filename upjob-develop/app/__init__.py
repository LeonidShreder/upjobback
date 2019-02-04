import json
import os

from flask import Flask
from flask_cors import CORS


ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'frontend')
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'frontend')

app = Flask(__name__, static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
CORS(app)

with open(os.path.abspath(os.path.join('app/config/config.json', ))) as f:
    config = json.load(f)

app.config['MAIL_SERVER'] = config['MAIL_SERVER']
app.config['MAIL_PORT'] = config['MAIL_PORT']
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

from app.rest_api import api
