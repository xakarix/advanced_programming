# 3. Eksperymentowanie z dużymi wartościami przesunięcia
# a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
# b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
# oryginalnego obrazu.

import numpy as np
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (image.shape[1]//2, image.shape[0]//2)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)

    M = np.float32([[1,0,cX + 100],[0,1,cY +200]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", shifted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



else:
    print("Błąd")