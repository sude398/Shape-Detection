import cv2
from shaping import Shape
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        #To store all squares and rectangles.
        self.rectangle_list = []
        self.square_list = []

    def detect_shapes(self, img, approx):
        #Finding each rectangle's aspect ratio to decide whether it's a square or not.
        x, y, w, h = cv2.boundingRect(approx)
        ratio = float(w / h)
        if len(approx) == 4:
            if 1.1 >= ratio >= 0.9:
                self.square_list.append(approx)
                cv2.putText(img, f"{len(self.square_list)} square found",(20, 600), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
            else:
                self.rectangle_list.append(approx)
                cv2.putText(img, f"{len(self.rectangle_list)} rectangle found",(20, 580), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    def contour_shapes(self, img, approx):
        #Drawing contours on a shape which has 4 corners.
        if len(approx) == 4:
            cv2.drawContours(img, [approx], -1, (0, 0, 0), 2)

    def print_shape_info(self, img):
        # Finding square's and rectangel's center and putting the information there.
        for square in self.square_list:
            M = cv2.moments(square)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Square", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "4 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)

        for rectangle in self.rectangle_list:
            M = cv2.moments(rectangle)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Rectangle", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "4 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)

