import cv2

class Enhance:

    def __init__(self, image_path):
        self.image_path = image_path

    def execute(self):
        self.read_image()
        self.gray_scale()
        self.thresholding()
        self.resize()
        return self.resized

    def read_image(self):
        self.img = cv2.imread(self.image_path)

      # Tornar imagem cinza (para facilitar leitura)
    def gray_scale(self):
        self.gray_scale_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Aplicar thresholding pra aumentar o contraste do texto em preto e branco de forma otimizada
    def thresholding(self):
        _, self.thresh = cv2.threshold(self.gray_scale_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Aumentar a imagem para deixar o texto mais facil de ler
    def resize(self):
        self.resized = cv2.resize(self.thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)


        