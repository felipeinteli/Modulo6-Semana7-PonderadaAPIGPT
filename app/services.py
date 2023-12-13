import logging
import openai
import requests
from app import models

openai.api_key = 'your-api-key-here'
class HistoryServices:

    def create_history(history_map):


        try:
            with models.HistoryDAO() as dao:
                dao.create_history(history_map)
            return True
        except (ValueError, TypeError) as e:
            return False
        except Exception as e:
            return False
        
    def find_all(self):
        try:
            with models.HistoryDAO() as dao:
                result = dao.find_all()
            return result
        except Exception as e:
            return []
        

    def chat_gpt_story(prompt):

        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Translate the following English text to French: '{}'",
        max_tokens=60
        )

        return response


