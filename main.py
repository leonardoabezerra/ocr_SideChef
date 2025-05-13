from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import pytesseract
import ProcessImage as process

app = FastAPI()

  # Rota para rodar o ocr
@app.post("/run-ocr/")
async def run_ocr(file: UploadFile = File(...)):
    try:
        # Ler arquivo
      file_contents = await file.read()

        # Converter para NumPy array e depois para formato cv2
      np_array = np.frombuffer(file_contents, np.uint8)
      image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
      
      if image is not None:
        # process_image = process.Enhance(image["path"])
        process_image = process.Enhance(image)
        processed_image = process_image.execute()

        extracted_text = pytesseract.image_to_string(processed_image, lang='por')
        print(extracted_text)

        process_image.show_steps()
        return extracted_text
      else: 
        return {"error": "Image not found"}

    except Exception as err:
       return {"error": f"File upload failed: {str(err)}"}
    

