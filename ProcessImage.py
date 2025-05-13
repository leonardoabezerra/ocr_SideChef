import cv2

class Enhance:

    def __init__(self, img):
        self.img = img

    def execute(self):
        self.canny_edge()
        self.gaussian_blur()
        self.gray_scale()
        self.thresholding()
        self.resize()
        return self.resized

        # Aplicar o filtro de Canny para detectar os arestas
    def canny_edge(self):
        self.canny = cv2.Canny(self.img, 100, 200, apertureSize=3, L2gradient=True)

        # Aplica desfoque Gaussiano para reduzir ruído
    def gaussian_blur(self):
        self.gaussian = cv2.GaussianBlur(self.img, (3, 3), 0)

        # Tornar imagem cinza (para facilitar leitura)
    def gray_scale(self):
        self.gray_scale_img = cv2.cvtColor(self.gaussian, cv2.COLOR_BGR2GRAY)

        # Aplicar thresholding pra aumentar o contraste do texto em preto e branco de forma otimizada
    def thresholding(self):
        _, self.thresh = cv2.threshold(self.gray_scale_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Aumentar a imagem para deixar o texto mais facil de ler
    def resize(self):
        self.resized = cv2.resize(self.thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)


        # Abrir janelas com as etapas de tratamento de imagem desejadas
    def show_steps(self):
        cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Thresholding", 800, 600)
        cv2.imshow("Thresholding", self.resized)

        cv2.namedWindow("Canny Edge", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Canny Edge", 800, 600)
        cv2.imshow("Canny Edge", self.canny)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


        