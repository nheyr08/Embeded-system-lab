import cv2
import numpy as np

if __name__ == '__main__':
    symbol = np.zeros((400, 700, 3), dtype=np.uint8)

    # TODO: change to white background and draw circles in symbol

    cv2.imshow('olympic symbol', symbol)

    cv2.waitKey()
    cv2.destroyAllWindows()
