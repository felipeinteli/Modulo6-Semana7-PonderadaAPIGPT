import threading
import requests
import json
import logging


def gerar_historias(prompt):

    KEY_GPT = "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"
    
    logging.info("Gerando histórias...API_GPT")
    headers = {"Authorization": f"Bearer {KEY_GPT}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    prompt_completo =  "Conte meu uma historia sobre: " + prompt
    logging.info("Prompt completo: %s", prompt_completo)

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": prompt_completo}]
    }

    body_mensagem = json.dumps(body_mensagem)
    logging.info("Body mensagem: %s", body_mensagem)

    try:
        requisicao_GPT = requests.post(link, headers=headers, data=body_mensagem)
        logging.info("Requisição GPT: %s", requisicao_GPT)
        requisicao_GPT.raise_for_status() 
        resposta_GPT = requisicao_GPT.json()
        logging.info("Resposta GPT: %s", resposta_GPT)
        
        if 'choices' in resposta_GPT and resposta_GPT['choices']:
            historia_atualizada = resposta_GPT['choices'][0]['message']['content']
            return historia_atualizada
        else:
            return "Resposta da GPT não contém o caminho esperado."

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"