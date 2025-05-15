from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import pytesseract
import ProcessImage as process
# pip install fastapi uvicorn python-multipart numpy opencv-python pytesseract
# also download Tesseract via web

app = FastAPI()

  # Endpoint to run OCR receiving target image as POST method
@app.post("/run-ocr/")
async def run_ocr(file: UploadFile = File(...)):
    try:
        # Read file
      file_contents = await file.read()

        # Convert to NumPy array then cv2 format
      np_array = np.frombuffer(file_contents, np.uint8)
      image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
      
      if image is None:
        return {"error": "Image not found"}

      process_image = process.Enhance(image)  # Initialize class with target image
      processed_image = process_image.execute()  # Run execute function

        # Extract and return OCR result
      extracted_text = pytesseract.image_to_string(processed_image, lang='por')
      cut_text = extracted_text.split('\n')[0]  # Fetch only first line

      print(cut_text.strip())  # For development only
      process_image.show_steps()  # Show desired steps from image enhancing process (development only)

      return [cut_text.strip()]
    
    except Exception as err:
       return {"error": f"File upload failed: {str(err)}"}
    

