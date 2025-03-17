# 6. Zamazywanie szczegółów na zdjęciu
# a. Znajdź w Internecie profilowe zdjęcie osoby.
# b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
# c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
# d. Niebieskim okręgiem obejmij dookoła twarz osoby.

import numpy as np
import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    red=(0,0,255)
    green=(0,255,0)
    blue=(255,0,0)

    cv2.circle(image,(1434,3298), 300, red, -1)
    cv2.circle(image,(2540,3282), 300, red, -1)

    cv2.rectangle(image,(1622,4297),(2499,4559), green, -1)

    cv2.circle(image,(cX,cY+300), 1500, blue, 20)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")

