import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("camera", frame)
    cv2.imshow("edges", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if cv2.getWindowProperty("camera", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()