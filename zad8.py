# 8. Obrót sekwencyjny
# a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
# końcowy.
# b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    rotate = imutils.rotate(image, 30)
    rotate = imutils.rotate(rotate, 30)
    rotate = imutils.rotate(rotate, 30)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", rotate)

    rotated = imutils.rotate(image, 90)


    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")