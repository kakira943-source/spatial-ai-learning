import cv2

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

print("color shape =", img.shape)
print("gray shape =", gray.shape)
print("edges shape =", edges.shape)

cv2.imshow("color", img)
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()