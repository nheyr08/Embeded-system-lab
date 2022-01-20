import os.path as path

import cv2

if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    print(f"The original image is {img.shape}, the pixels are type: {img.dtype}")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(path.join('images', 'Lenna.png'), img)
    print(f"After conversion, the grayscale image is {img.shape}, the pixels are type: {img.dtype}")
