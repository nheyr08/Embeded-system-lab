import os.path as path

import cv2

if __name__ == '__main__':
    crazydog = cv2.imread(path.join('images', 'crazydog.jpg'))
    puipui = cv2.imread(path.join('images', 'puipui.jpg'))

    # TODO: merge two images

    cv2.imshow('result', crazydog)

    cv2.waitKey()
    cv2.destroyAllWindows()
