# 5. Automatyczne skalowanie na podstawie szerokości
# a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
# b. Użyj imutils.resize() .

import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = imutils.resize(image,width=500)

    cv2.imshow("photo", image)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")