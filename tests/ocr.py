import numpy as np
import cv2
import pytesseract

class ImageProcess:
    def __init__(self, image_path):
        self.image_og = cv2.imread(image_path)
        if self.image_og is None:
            raise ValueError(f"Não foi possível carregar a imagem do caminho: {image_path}")
        self._image_mathlike = self.image_og
        self._extarcted_text = None

    @property
    def image_mathlike(self):
        return self._image_mathlike
    
    @image_mathlike.setter
    def image_mathlike(self, value):
        self._image_mathlike = value

    @property
    def extracted_text(self):
        return self._extarcted_text
    
    @extracted_text.setter
    def extracted_text(self, value):
        self._extarcted_text = value


    def reset_image(self):
        self.image_mathlike = self.image_og

    def noise_cancel(self):
        self.image_mathlike = cv2.GaussianBlur(self.image_mathlike, (3, 3), 2.5)

    def canny_use(self):
        self.image_mathlike = cv2.Canny(self.image_mathlike, 300, 400)

    def threshold(self):
        gray = cv2.cvtColor(self.image_mathlike, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.image_mathlike = thresh

    def resize(self):
        self.image_mathlike = cv2.resize(self.image_mathlike, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    def show_img(self):
        if np.any(self.image_mathlike) == True:
            cv2.imshow("Imagem", self.image_mathlike)
            k = cv2.waitKey(0)
        else:
            print("Erro")    

    def use_ocr(self):
        self.extracted_text = pytesseract.image_to_string(self.image_mathlike, lang='por')
        print(self.extracted_text)


def main():
    processor = ImageProcess("/home/winny/codes/UNB/MDS/teste_app_receitas/img/italac.jpeg")
    processor.resize()
    processor.noise_cancel()
    processor.threshold()
    processor.canny_use()
    processor.use_ocr()
    processor.show_img()

main()