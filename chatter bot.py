from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
bot = ChatBot('Tech Support Bot')

# Create a new trainer for the chat bot
trainer = ChatterBotCorpusTrainer(bot)

# Train the bot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Define a function for getting the bot's response
def get_bot_response(user_input):
    return bot.get_response(user_input)

# Start a conversation with the bot
print("Tech Support Bot: Hi! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Tech Support Bot: Goodbye!")
        break
    response = get_bot_response(user_input)
    print("Tech Support Bot:", response)
