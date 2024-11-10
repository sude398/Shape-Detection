import cv2
from shaping import Shape
class Circle(Shape):
    def __init__(self):
        super().__init__()
        #To store all circles and ellipses.
        self.circle_list = []
        self.ellipse_list = []

    def detect_shapes(self, img, approx):
        #If shape has approximately 6-15 corners it will be detected as an ellipse.
        if 6 < len(approx) < 15:
            self.ellipse_list.append(approx)
            cv2.putText(img, f"{len(self.ellipse_list)} ellipse found",(200, 580), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
        elif 15 <= len(approx):
            self.circle_list.append(approx)
            cv2.putText(img, f"{len(self.circle_list)} circle found",(200, 580), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    def contour_shapes(self, img, approx):
        if len(approx) < 15:
            cv2.drawContours(img, [approx], -1, (0, 0, 0), 2)

    def print_shape_info(self, img):
        # Finding circle's and ellipse's center and putting the information there.
        for circle in self.circle_list:
            M = cv2.moments(circle)
            if M["m00"] > 0:  # Avoid division by zero
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Circle", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "0 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)

        for ellipse in self.ellipse_list:
            M = cv2.moments(ellipse)
            #To avoid division by zero
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Ellipse", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "0 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
