from flask import Flask

from . import api
from . import chatbot

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.chatbot_api , url_prefix='/chatbot')
    return app
