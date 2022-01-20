import os.path as path

import cv2


def convert_to_pencil_sketch(rgb_image):
    # TODO: finish this filter
    result = rgb_image
    return result


if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    sketch = convert_to_pencil_sketch(img)

    cv2.imshow("Sketch", sketch)

    cv2.waitKey()
    cv2.destroyAllWindows()
