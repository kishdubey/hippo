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
'Hello',
'Hello, I\'m Hippo! How are you feeling today?',
'Not too bad',
'How would you describe your day?',
'Fun but tiring!',
'What would make you feel better right now?',
'Here are some resources that can help, https://www.ottawapublichealth.ca/en/public-health-topics/mental-health.aspx'
'Here are some resources that can help, https://www.ottawapublichealth.ca/en/public-health-topics/mental-health.aspx'
'Here are some resources that can help, https://www.ottawapublichealth.ca/en/public-health-topics/mental-health.aspx'
'Here are some resources that can help, https://www.ottawapublichealth.ca/en/public-health-topics/mental-health.aspx'
])
