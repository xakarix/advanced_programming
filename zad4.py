# 4. Tworzenie własnego "filtra Instagram":
# a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego +10.
# b. Sprawdź, jak zmienia się obraz.

import cv2
import numpy as np

image = cv2.imread("layla.png")

if image is not None:
    (b,g,r) = cv2.split(image)

    r = cv2.add(r, 30)
    g = cv2.subtract(g, -20)
    b = cv2.add(b, 10)

    insta_image = cv2.merge([b,g,r])

    cv2.imshow("Photo", image)
    cv2.imshow("Photo insta", insta_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")