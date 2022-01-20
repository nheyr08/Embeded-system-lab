import cv2
import numpy

if __name__ == '__main__':
    black = numpy.zeros((100, 200, 3), dtype=numpy.uint8)
    cv2.imshow('empty img', black)

    blue = black.copy()
    blue[:, :, 0] = 255
    cv2.imshow('blue', blue)

    red_green = black.copy()
    red_green[:, :100, 2] = 255
    red_green[:, 100:, 1] = 255
    cv2.imshow('red_green', red_green)

    cv2.waitKey()
    cv2.destroyAllWindows()
