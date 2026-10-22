import cv2

# 使用するArUco辞書
dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

# 検出器を作る
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # ArUcoマーカーを探す
    corners, ids, rejected = detector.detectMarkers(frame)

    # 見つかったら描画
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    cv2.imshow("ArUco Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if cv2.getWindowProperty(
        "ArUco Detection",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

cap.release()
cv2.destroyAllWindows()