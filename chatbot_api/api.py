import json
from flask import Blueprint,render_template,request
from . import chatbot
 
chatbot_api = Blueprint('chatbot_api', __name__)

@chatbot_api.route("/get_response", methods=['GET'])
def get_response():
    try:
        chat = request.args.get('chat', '')
        if chat:
            resp = chatbot.get_response(chat)
            return json.dumps({"chatbot_resp": resp})
        raise Exception("Failed to get response from chatbot")
    except Exception as e:
        return json.dumps({"error": str(e)})
    