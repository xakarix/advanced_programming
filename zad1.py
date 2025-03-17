# 1. Podstawowe przesunięcie
# a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
# b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy
# transformacji M oraz cv2.warpAffine.
# c. Wyświetl wynik.

import numpy as np
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)

    M = np.float32([[1,0,30],[0,1,40]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", shifted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



else:
    print("Błąd")