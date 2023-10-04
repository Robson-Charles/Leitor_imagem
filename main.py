from flask import Flask, request, jsonify
from Converter_imagem import escrever_arquivo
app = Flask(__name__)
import os
@app.route
def get_texto(svg):
    return jsonify(escrever_arquivo.criar_txt(svg))
api_keys = {
    'client1': 'rob',

}
# app.py

#from process_file import process_text_file

app = Flask(__name__)

@app.route('/captcha', methods=['POST'])
def process():
    api_key = request.headers.get('X-API-Key')  # Obtenha a chave da solicitação

    if api_key not in api_keys.values():
        return jsonify({'error': 'Chave de API inválida'}), 401
    # Verifica se o arquivo de texto foi enviado como parâmetro
    if 'file' not in request.files:
        return jsonify({'error': 'Arquivo não especificado'}), 400

    file = request.files['file']

    # Verifique se o nome do arquivo é vazio
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo vazio'}), 400

    try:
        # Salve o arquivo no sistema de arquivos (opcional)
        # O exemplo a seguir salva o arquivo no diretório de upload
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)

        # Chame a função para processar o arquivo e obter o resultado
        result = get_texto(file_path)

        # Exclua o arquivo após o processamento, se necessário
        os.remove(file_path)

        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
