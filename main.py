from flask import Flask, jsonify, request
from Converter_imagem import escrever_arquivo
#app = Flask(__name__)

#@app.route
#def get_texto(svg):
    #return jsonify(Converter_imagem.escrever_arquivo.criar_txt(svg))
# app.py
#from flask import Flask, request, jsonify
#from process_file import process_text_file

app = Flask(__name__)
api_keys = {
    'client1': 'rob',

}
@app.route('/captcha', methods=['GET'])
def process():
    api_key = request.headers.get('X-API-Key')  # Obtenha a chave da solicitação

    if api_key not in api_keys.values():
        return jsonify({'error': 'Chave de API inválida'}), 401

    # Verifica se o arquivo de texto foi enviado como parâmetro
    file = request.args.get('file')

    if not file:
        return jsonify({'error': 'Arquivo não especificado'}), 400

    try:
        # Chama a função para processar o arquivo
        result = escrever_arquivo.criar_txt(file)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
