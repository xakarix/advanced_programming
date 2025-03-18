# 8. Efekty przy skalowaniu w górę
# a. Powiększ obraz 4× używając INTER_CUBIC i INTER_LANCZOS4 .
# b. Porównaj ostrość obrazu w obu przypadkach.

import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized1 = cv2.resize(image,(w*4,h*4), interpolation=cv2.INTER_LINEAR)
    resized2 = cv2.resize(image,(w*4,h*4), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("resized1", resized1)
    cv2.imshow("resized2", resized2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")