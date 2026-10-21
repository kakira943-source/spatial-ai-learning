import cv2

img = cv2.imread("images/test.jpg")

print("color shape =", img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("gray shape =", gray.shape)

cv2.imshow("color", img)
cv2.imshow("gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()