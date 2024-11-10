import cv2
from shaping import Shape
class Pentagon(Shape):
    def __init__(self):
        super().__init__()
        #To store all pentagons.
        self.pentagon_list = []

    def detect_shapes(self, img, approx):
        if len(approx) == 5:
            self.pentagon_list.append(approx)
            cv2.putText(img, f"{len(self.pentagon_list)} pentagon found",(200, 620), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

    def contour_shapes(self, img, approx):
        if len(approx) == 5:
            cv2.drawContours(img, [approx], -1, (0, 0, 0), 2)

    def print_shape_info(self, img):
        # Finding pentagon's center and putting the information there.
        for pentagon in self.pentagon_list:
            M = cv2.moments(pentagon)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(img, "Pentagon", (cx-60, cy), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, "5 corners", (cx-60 , cy+30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)