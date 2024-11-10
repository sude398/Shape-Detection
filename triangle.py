import cv2
from shaping import Shape
class Triangle(Shape):
    def __init__(self):
        super().__init__()
        #To store all triangles(if there is same shape more than 1 it will detect).
        self.triangle_list = []

    def detect_shapes(self, img, approx):
        #If shape has 3 certain points it's triangle.
        if len(approx) == 3:
            self.triangle_list.append(approx)
            cv2.putText(img, f"{len(self.triangle_list)} triangle found",(20, 620), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    def contour_shapes(self, img, approx):
        if len(approx) == 3:
            #To draw contours around triangles
            cv2.drawContours(img, [approx], -1, (0, 0, 0), 2)

    def print_shape_info(self, img):
        for triangle in self.triangle_list:
            #Finding triangle's center and putting the information there.
            M = cv2.moments(triangle)
            # To avoid division by zero
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Triangle", (cx-50, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "3 corners", (cx-50 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)

