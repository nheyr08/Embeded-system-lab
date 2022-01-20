import os.path as path

import cv2

if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    face = img[100:240, 100:240, :]   # Copy Lenna's face
    img[0:140, 0:140, :] = face       # Paste on top left corner
    cv2.imshow('new img', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
