from robo import *
from flask import Flask, jsonify
from flask_cors import CORS 
import time
time.clock = time.time

robo = iniciar()
chatBot = Flask(__name__)
CORS(chatBot) 

@chatBot.route("/resposta/<mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)

    if resposta.confidence >= CONFIANCA_MINIMA:
        return jsonify({'resposta': resposta.text})
    else:
        return jsonify({'resposta': "Desculpe, mas no momento não tenho informação suficiente para responder essa pergunta"})


if __name__ == "__main__":
    chatBot.run(debug=True, host='0.0.0.0', port=5000)