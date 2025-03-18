# 2. Przycięcie dolnej połowy obrazu
# a. Podziel obraz na dwie równe części (górną i dolną).
# b. Wyświetl tylko dolną połowę.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    up = image[0:h//2, :]
    down = image[h//2:h, :]

    cv2.imshow("Photo", down)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")