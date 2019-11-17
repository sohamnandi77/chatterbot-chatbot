from chatterbot import ChatBot  # pip install chatterbot
from chatterbot.trainers import ListTrainer  # method to train chatbot
from train import start_trainer

# import logging
# logging.basicConfig(level=logging.INFO)

bad_chars = [";", ":", "!", "@", "#", "$", "%", "^", "&", "(", ")", "?",",", ".", "~", "`", "[", "]", "{", "}", "-", "_"] # initializing bad_chars_list

bot = ChatBot(
    'Example Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        }])

trainer = ListTrainer(bot)  # set the trainer


def chatbot():
    while True:
        request = input("you: ").lower()
        for i in bad_chars:
            request = request.replace(i, '')  # using replace() to remove bad_chars
        request_que = request.split(" ")
        response = bot.get_response(request)
        print("bot: " + str(response))


chatbot()
