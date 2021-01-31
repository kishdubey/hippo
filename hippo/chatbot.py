# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Hippo',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello, I\'m Hippo! How was your day today?',
'It was pretty bad',
'How were you feeling?',
'Not good',
'What would make you feel better?',
'Sleep',
])

trainer.train([
'Hello',
'Hello, I\'m Hippo! How was your day today?',
'I had a bad day. I\'ve been feeling anxious and stressed out',
'What made you feel that way?',
'Pressure to meet deadlines at work',
'Do you want to talk about it?',
'Yes',
])

trainer.train([
'Hello',
'Hello, I\'m Hippo! How are you feeling today?',
'Not too bad',
'How would you describe your day?',
'Fun but tiring!',
'What would make you feel better right now?',
'The weekend',
])

# Get a response to the input text 'I would like to book a flight.'
# response = bot.get_response('I have a complaint.')

li = []

def addToList(str):
	li.append(str)

while True:
    request=input('You:')
    addToList(request)
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)

print(li)