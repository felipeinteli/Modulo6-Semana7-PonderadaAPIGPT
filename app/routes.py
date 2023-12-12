from flask import request, jsonify
from app import app, db
from app.models import Historia
import requests  

@app.route('/historia', methods=['POST'])
def criar_historia():
    data = request.json
    prompt = data['prompt']

    # Aqui, você precisa implementar a lógica para interagir com a API do ChatGPT
    # Por exemplo:
    resposta_chatgpt = requests.post('URL_DA_API_CHATGPT', json={'prompt': prompt})

    # Supondo que a resposta da API seja um JSON com uma chave 'response'
    resposta = resposta_chatgpt.json().get('response')

    nova_historia = Historia(prompt=prompt, resposta=resposta)
    db.session.add(nova_historia)
    db.session.commit()

    return jsonify({'id': nova_historia.id, 'prompt': prompt, 'resposta': resposta}), 201
