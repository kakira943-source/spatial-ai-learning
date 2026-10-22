import cv2
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

marker = cv2.aruco.generateImageMarker(
    dictionary,
    0,
    400
)

image = np.ones((500, 500), dtype=np.uint8) * 255

image[50:450, 50:450] = marker

cv2.imwrite("images/marker_0.png", image)