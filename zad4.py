# 4. Obrót o dowolny kąt
# a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
# b. Wyświetl wynik.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    x = int(input("Podaj kąt: "))

    M = cv2.getRotationMatrix2D((cX,cY), x, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")