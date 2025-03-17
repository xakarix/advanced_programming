# 1. Obrót o 45 stopni
# a. Wczytaj obraz i wykonaj obrót o 45 stopni wokół jego środka.
# b. Wyświetl obraz przed i po rotacji.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)

    M = cv2.getRotationMatrix2D((cX,cY), 45,1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")