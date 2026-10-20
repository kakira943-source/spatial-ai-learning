import cv2

img = cv2.imread("images/test.jpg")

print("shape =", img.shape)

h, w, c = img.shape

print("height =", h)
print("width  =", w)
print("channel =", c)

# 画像中央の画素
pixel = img[h // 2, w // 2]

print("center pixel =", pixel)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()