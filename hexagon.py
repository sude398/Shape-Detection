import cv2
from shaping import Shape
class Hexagon(Shape):
    def __init__(self):
        super().__init__()
        #To store all hexagons.
        self.hexagon_list = []

    def detect_shapes(self, img, approx):
        if len(approx) == 6:
            self.hexagon_list.append(approx)
            #Putting text on image about how many specific shapes are found.
            cv2.putText(img, f"{len(self.hexagon_list)} hexagon found",(200, 600), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    def contour_shapes(self, img, approx):
        if len(approx) == 6:
            cv2.drawContours(img, [approx], -1, (0, 0, 0), 2)

    def print_shape_info(self, img):
        # Finding hexagon's center and putting the information there.
        for hexagon in self.hexagon_list:
            M = cv2.moments(hexagon)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Hexagon", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "6 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
