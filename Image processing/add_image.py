import os.path as path

import cv2

if __name__ == '__main__':
    castle = cv2.imread(path.join('images', 'castle.jpg'))
    rain = cv2.imread(path.join('images', 'rain.jpg'))

    result = cv2.addWeighted(castle, 0.7, rain, 0.9, 0.)
    cv2.imshow("Castle Rain", result)
    larger = cv2.resize(result, dsize=(300, 300))  # Resize to 300x300
    double_size = cv2.resize(result, dsize=None, fx=2, fy=2)  # Double x and y dimensions
    cv2.imshow("Larger", larger)
    cv2.imshow("double_size", double_size)

    cv2.waitKey()
    cv2.destroyAllWindows()
