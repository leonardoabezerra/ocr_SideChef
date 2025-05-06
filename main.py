import cv2
import pytesseract

  # Abrir imagem com o OpenCV
image_path = r".\img\informacao-nutricional.jpg"
img = cv2.imread(image_path)

  # Tornar imagem cinza (para facilitar leitura)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Aplicar thresholding pra aumentar o contraste do texto em preto e branco de forma otimizada
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

  # Aumentar a imagem para deixar o texto mais facil de ler
resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

  # Extrai o texto da imagem usando o tesseract
extracted_text = pytesseract.image_to_string(resized, lang='por')

print(extracted_text)
