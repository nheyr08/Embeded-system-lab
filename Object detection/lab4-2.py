import cv2

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier(
        './cascades/haarcascade_frontalface_default.xml')

    img = cv2.imread('faces_2.jpg')
    img = cv2.resize(img, dsize=None, fx=0.8, fy=0.8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 3)
    for (x, y, w, h) in faces:
        if w > 40:
            continue
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('lab4-2', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
