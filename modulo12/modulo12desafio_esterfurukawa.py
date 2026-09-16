from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá, mundo!"}), 200

@app.route('/api/somar', methods=['POST'])
def somar():
    dados = request.get_json()
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({"erro": "Entrada inválida"}), 400
    resultado = dados['a'] + dados['b']
    return jsonify({"resultado": resultado}), 200

if __name__ == '__main__':
    app.run(debug=True)