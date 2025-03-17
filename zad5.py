# 5. Obrót o 180 stopni za pomocą imutils.rotate
# a. Skorzystaj z imutils.rotate , aby obrócić obraz o 180 stopni.
# b. Wyświetl wynik.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    rotated = imutils.rotate(image, 180)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")