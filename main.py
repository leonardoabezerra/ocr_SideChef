from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import ProcessImage as process
import pytesseract

app = FastAPI()

  # Conexão com MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["test-ocr"]
collection = db["img"]
  
  # Obs: no meu mongodb local tenho o seguinte objeto: { _id: ObjectId(681e6890ecd3abda3c6c4bd1), path: "./img/italac.jpeg"}

  # Rota home para praticidade de teste do ocr
@app.get("/")
async def redirect():
  # Redireciona imediatamente para a rota run-ocr com o id de teste já aplicado
  return RedirectResponse(url="/run-ocr/681e6890ecd3abda3c6c4bd1")  # ObjectId do italac.jpeg

  # Rota para rodar o ocr
@app.get("/run-ocr/{image_id}")  # Passar id da imagem como parâmetro 
async def run_ocr(image_id: str):
    try:
      image = await collection.find_one({"_id": ObjectId(image_id)})
      if image:
        process_image = process.Enhance(image["path"])
        processed_image = process_image.execute()

        extracted_text = pytesseract.image_to_string(processed_image, lang='por')
        print(extracted_text)
        return extracted_text
      else: {"erro": "Imagem nao encontrada"}

    except Exception as err:
       return {"erro": f"Erro de consulta do ID: {str(err)}"}
    

