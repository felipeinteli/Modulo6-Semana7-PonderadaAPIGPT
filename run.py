import logging
from flask import Flask, request, jsonify
from app.services import HistoryServices
import json

app = Flask(__name__)
history_services = HistoryServices()


@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    try:
        prompt = json.loads(request.data)
        success = HistoryServices.create_history(prompt)
        return jsonify({"status": "success" if success else "failed"}), 200
    except json.JSONDecodeError:
        logging.error("JSON inválido recebido.")
        return jsonify({"status": "error", "message": "JSON inválido"}), 400
    except Exception as e:
        logging.error(f"Erro ao criar empregado: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/get_all', methods=['GET'])
def get_historys():
    try:
        historys = HistoryServices.find_all()
        return jsonify({"status": "success", "historys": historys}), 200
    except Exception as e:
        logging.error(f"Erro ao criar empregado: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    
if __name__ == '__main__':
    app.run(debug=True)