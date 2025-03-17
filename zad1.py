# 1. Rysowanie linii
# a. Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu.
# Grubość linii: 2 px.

import numpy as np
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)


    blue=(255,0,0)

    cv2.line(image,(cX,cY), (w,h), blue, 2)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")

