# coding=utf-8

import os

from flask import Flask
from app.database import init_db

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))

app = Flask(__name__)
init_db()
