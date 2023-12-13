import logging
import openai
import requests
from app import models

from dotenv import load_dotenv
import os


load_dotenv() 



class HistoryServices:

    def create_history(prompt):
        response = HistoryServices.chat_gpt_story(prompt)
        history = response['choices'][0]['text']
        history_map = {
            'prompt': prompt['prompt'],
            'resposta': history
        }
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
        

    def chat_gpt_story(json):
        prompt = json['prompt']
        openai.api_key = os.getenv("API_KEY")
        prompt = f"Conte meu uma história sobre: '{prompt}'"
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200
        )

        return response


