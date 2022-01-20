import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("star.jpg")
    cv2.imshow("original", img)
    img_h = img.shape[0]
    img_w = img.shape[1]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Some manual preprocessing
    ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                155, 255, cv2.THRESH_BINARY)
    thresh = cv2.Canny(thresh, 200, 200)
    clean = np.zeros((img_h, img_w), dtype=np.uint8)
    clean[196:420, 225:454] = thresh[196:420, 225:454]

    contours, hierarchy = cv2.findContours(clean, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    # Extract the longest contour
    star = max(contours, key=lambda c: c.shape[0])

    img = cv2.drawContours(img, [star], -1, (0, 0, 255), 2)  # The contour argument must be a list

    cv2.imshow("lab4-1", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
