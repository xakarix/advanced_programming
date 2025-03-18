# 6. Automatyczne skalowanie na podstawie wysokości
# a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
# b. Wyświetl wynik.

import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = imutils.resize(image,height=400)

    cv2.imshow("photo", image)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")