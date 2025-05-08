import cv2
import ProcesssarImagem as process
import pytesseract

  # Abrir imagem com o OpenCV
image_path = r".\img\italac.jpeg"

  # Chamar a classe para processar a imagem
processar_imagem = process.Processar(image_path)
imagem_processada = processar_imagem.execute()

  # Extrai o texto da imagem usando o tesseract
extracted_text = pytesseract.image_to_string(imagem_processada, lang='por')

print(extracted_text)
