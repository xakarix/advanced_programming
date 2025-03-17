# 4. Wykorzystanie funkcji imutils.translate
# a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
# imutils.translate .
# b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
# Czy zauważyłeś różnice?

import numpy as np
import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)

    shifted = imutils.translate(image, 100, 50)

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", shifted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



else:
    print("Błąd")