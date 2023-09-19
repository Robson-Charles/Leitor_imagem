from fastapi import FastAPI, UploadFile
from Converter_imagem import escrever_arquivo
app = FastAPI()
from fastapi.responses import JSONResponse
@app.post("/Lucas")
async def root(file: UploadFile):
    #print(file.file.read().decode('utf-8'))

    texto = escrever_arquivo.criar_txt(file.file.read().decode('utf-8'))
    print(texto)
    return JSONResponse(content={"mensagem": texto}, status_code=200)
