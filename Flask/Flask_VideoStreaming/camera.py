import cv2
cap = cv2.VideoCapture(0)
cap.read()
cap.set(3,640)
cap.set(4,480)
while True:
    success, image = cap.read()
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()