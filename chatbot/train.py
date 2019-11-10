from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ListTrainer #method to train chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

def start_trainer():
    bot = ChatBot(
    'Example Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }])
    trainer = ListTrainer(bot) #set the trainer
    for _file in os.listdir('files'):
        chats = open('files/' + _file, 'r').readlines()
        trainer.train(chats)

try:
    file=open("file.txt", 'r')
except FileNotFoundError:
    start_trainer();
    file=open("file.txt",'w')
