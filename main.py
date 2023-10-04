from flask import Flask, jsonify, request
from Converter_imagem import escrever_arquivo
import os

app = Flask(__name__)
api_keys = {
    'client1': 'rob',

}
@app.route('/captcha', methods=['POST'])
def process():
    api_key = request.headers.get('X-API-Key')  # Obtenha a chave da solicitação

    if api_key not in api_keys.values():
        return jsonify({'error': 'Chave de API inválida'}), 401

    # Verifica se o arquivo de texto foi enviado como parâmetro
    file = request.files['file']
    try:
        # Salve o arquivo no sistema de arquivos (opcional)
        # O exemplo a seguir salva o arquivo no diretório de upload
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)

        # Chame a função para processar o arquivo (substitua 'escrever_arquivo' pela função apropriada)
        result = escrever_arquivo.melhorar_font(file_path)
        
        # Exclua o arquivo após o processamento, se necessário
        os.remove(file_path)

        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
