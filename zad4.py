# 4. Złożona figura
# a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
# px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
# Wszystko powinno być wycentrowane na obrazie.

import cv2
import numpy as np

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)


    red=(0,0,255)
    blue=(255,0,0)

    cv2.rectangle(image,(cX-50,cY-50), (cX+50,cY+50), blue, 4)
    cv2.circle(image,(cX,cY), 30, red, 4)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")



