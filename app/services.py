import logging
import openai
import requests
from app import models



class HistoryServices:

    def create_history(prompt):
        try:
            logging.info("Criando história...Service")
            response = HistoryServices.chat_gpt_story(prompt)
            logging.info("Passou função chatgpt %s", response)
            history = response['choices'][0]['text']
            logging.info("history %s", history)
            history_map = {
                'prompt': prompt['prompt'],
                'resposta': history
            }
            logging.info("History_map: %s", history_map)
            try:
                logging.info("Criando história...DAO")
                with models.HistoryDAO() as dao:
                    dao.create_history(history_map)
                return True
            except (ValueError, TypeError) as e:
                return False
            except Exception as e:
                return False
        except Exception as e:
            logging.error(f"Erro ao criar na função create_history: {e}")
            return False


        
    def find_all(self):
        try:
            with models.HistoryDAO() as dao:
                result = dao.find_all()
            return result
        except Exception as e:
            return []
        

    def chat_gpt_story(json):
        logging.info("Entrou função chatgpt")
        prompt = json['prompt']
        logging.info("Prompt JSON: %s", prompt)
        openai.api_key = "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"
        prompt = f"Conte meu uma história sobre: '{prompt}'"
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
            )
            return response
        except Exception as e:
            logging.error(f"Erro ao criar história na função gpt: {e}")
            return False

        


