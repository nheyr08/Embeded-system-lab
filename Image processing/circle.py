import os.path as path

import cv2

if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    cv2.circle(img, (180, 190), 50, (255, 255, 0), thickness=5)
    cv2.imshow("Result", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
