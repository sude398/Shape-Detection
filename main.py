import cv2
from triangle import Triangle
from rectangle import Rectangle
from pentagon import Pentagon
from hexagon import Hexagon
from circle import Circle

img = cv2.imread("shapes.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#To detect edges in an image
edges = cv2.Canny(gray, 100, 200)
#To find contours in an image which are defined as curve between 2 points.
contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
for contour in contours:
    #Approximation is sensitive to find most certain corners.
    # Approximation tolerance
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    #All shape's data is stored in shapes list and is being iterated.
    shapes = [Triangle(), Rectangle(), Pentagon(), Hexagon(), Circle()]
    for shape in shapes:
        shape.detect_shapes(img, approx)
        shape.contour_shapes(img, approx)
        shape.print_shape_info(img)
#To show the final image
cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()