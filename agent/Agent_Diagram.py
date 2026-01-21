# You may need to add your working directory to the Python path. To do so, uncomment the following lines of code
# import sys
# sys.path.append("/Path/to/directory/besser-agentic-framework") # Replace with your directory path

import logging
import operator

from besser.agent.core.agent import Agent
from besser.agent.nlp.llm.llm_huggingface import LLMHuggingFace
from besser.agent.nlp.llm.llm_huggingface_api import LLMHuggingFaceAPI
from besser.agent.nlp.llm.llm_openai_api import LLMOpenAI
from besser.agent.nlp.llm.llm_replicate_api import LLMReplicate
from besser.agent.core.session import Session
from besser.agent.nlp.intent_classifier.intent_classifier_configuration import LLMIntentClassifierConfiguration, SimpleIntentClassifierConfiguration
from besser.agent.nlp.speech2text.openai_speech2text import OpenAISpeech2Text
from besser.agent.nlp.text2speech.openai_text2speech import OpenAIText2Speech

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Create the bot
agent = Agent('Agent_Diagram')
# Load bot properties stored in a dedicated file
agent.load_properties('config.ini')

# Define the platform your chatbot will use


platform = agent.use_websocket_platform(use_ui=True)


# LLM instantiation based on config['llm']







##############################
# INTENTS
##############################

##############################
# STATES
##############################



# RUN APPLICATION

if __name__ == '__main__':
    agent.run()