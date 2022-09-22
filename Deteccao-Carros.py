import cv2

carCascade = cv2.CascadeClassifier("carx.xml")

captura = cv2.VideoCapture("dataset_video1.avi")

'''
while True:
    ret, frame = captura.read()
    cv2.imshow("imagem", frame)

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    carros = carCascade.detectMultiScale(image_gray, 1.1, 1)

    for (x, y, w, h) in carros:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
'''


while True:
    ret, img = captura.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = carCascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
