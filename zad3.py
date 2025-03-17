# 3. Obrót wokół narożnika
# a. Obróć obraz o 30 stopni względem lewego górnego narożnika (0,0).
# b. Wyświetl wynik.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    M = cv2.getRotationMatrix2D((0,0), 30,1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")