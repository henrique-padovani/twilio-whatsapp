

from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer




def getChatBot(chatbotName):

    chatbot = ChatBot(chatbotName)
    # Create a new trainer for the chatbot
    # trainer = ChatterBotCorpusTrainer(chatbot)
    # # Train the chatbot based on the english corpus
    # trainer.train("chatterbot.corpus.english")
    # # Train based on english greetings corpus
    # trainer.train("chatterbot.corpus.english.greetings")
    # # Train based on the english conversations corpus
    # trainer.train("chatterbot.corpus.english.conversations")
    # Get a response to an input statement
    return chatbot

# chatbot.get_response("Hello, how are you today?")
# while True:
#     quest = input('You: ')
#     resp = chatbot.get_response(quest)
#     print('Bot: ' + str(resp))