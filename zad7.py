# 7. Porównanie warpAffine i imutils.rotate
# a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
# imutils.rotate .
# b. Porównaj wyniki i zwróć uwagę na różnice.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    M = cv2.getRotationMatrix2D((cX,cY), 60,1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", rotated)

    rotate = imutils.rotate(image, 60)


    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", rotate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")