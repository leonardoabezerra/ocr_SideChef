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

        # Aplly Canny edge filter (currently unused)
    def canny_edge(self):
        self.canny = cv2.Canny(self.img, 100, 200, apertureSize=3, L2gradient=True)

        # Apply gaussian blur to reduce noise
    def gaussian_blur(self):
        self.gaussian = cv2.GaussianBlur(self.img, (3, 3), 0)

        # Gray scale image to facilitate reading
    def gray_scale(self):
        self.gray_scale_img = cv2.cvtColor(self.gaussian, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to enhance optimized contrast in black and white
    def thresholding(self):
        _, self.thresh = cv2.threshold(self.gray_scale_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Reescale the image to make it easier to read
    def resize(self):
        self.resized = cv2.resize(self.thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)


        # Pop up windows with desired steps (used for development only)
    def show_steps(self):
        cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Thresholding", 800, 600)
        cv2.imshow("Thresholding", self.resized)

        cv2.namedWindow("Canny Edge", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Canny Edge", 800, 600)
        cv2.imshow("Canny Edge", self.canny)

        cv2.waitKey(0)  # Wait key press to close windows
        cv2.destroyAllWindows()


        