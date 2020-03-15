# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create a new chat bot
_chatbot = ChatBot(
        'Somebody',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
        )

# Get a response
def get_response(chat):
    return str(_chatbot.get_response(chat))

# Training the ChatBot
def train_default(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer.train("chatterbot.copus.chinese")

if __name__ == "__main__":
    train_default(_chatbot)
    print(get_response("你好"))
