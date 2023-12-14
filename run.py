import logging
from fastapi import FastAPI, HTTPException
from app.services import HistoryServices
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
history_services = HistoryServices()

class Prompt(BaseModel):
    prompt: str

@app.post('/send_prompt')
async def send_prompt(prompt: Prompt):
    try:
        logging.info("Prompt type: %s", type(prompt.prompt))
        success = await HistoryServices.create_history(prompt.prompt)
        return {"status": "success" if success else "failed"}
    except Exception as e:
        logging.error(f"Erro ao criar empregado: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/get_all')
async def get_historys():
    try:
        historys = await HistoryServices.find_all()
        return {"status": "success", "historys": historys}
    except Exception as e:
        logging.error(f"Erro ao criar empregado: {e}")
        raise HTTPException(status_code=500, detail=str(e))

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# import logging
# from flask import Flask, request, jsonify
# from app.services import HistoryServices
# import json

# app = Flask(__name__)
# history_services = HistoryServices()


# @app.route('/send_prompt', methods=['POST'])


# def send_prompt():
#     try:
#         response = json.loads(request.data)
#         prompt = response['prompt']
#         logging.info("Prompt type: %s", type(prompt))
#         success = HistoryServices.create_history(prompt)
#         return jsonify({"status": "success" if success else "failed"}), 200
#     except json.JSONDecodeError:
#         logging.error("JSON inválido recebido.")
#         return jsonify({"status": "error", "message": "JSON inválido"}), 400
#     except Exception as e:
#         logging.error(f"Erro ao criar empregado: {e}")
#         return jsonify({"status": "error", "message": str(e)}), 500
    
# @app.route('/get_all', methods=['GET'])
# def get_historys():
#     try:
#         historys = HistoryServices.find_all()
#         return jsonify({"status": "success", "historys": historys}), 200
#     except Exception as e:
#         logging.error(f"Erro ao criar empregado: {e}")
#         return jsonify({"status": "error", "message": str(e)}), 500



# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    
# if __name__ == '__main__':
#     app.run(debug=True)