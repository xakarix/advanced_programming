# 1. Zmniejszenie obrazu o połowę
# a. Wczytaj obraz i zmniejsz jego szerokość oraz wysokość o 50%.
# b. Wyświetl wynik.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = cv2.resize(image,(w // 2, h // 2), interpolation=cv2.INTER_AREA)


    cv2.imshow("photo", image)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")