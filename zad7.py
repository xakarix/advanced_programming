# 7. Efekty przy skalowaniu w dół
# a. Zmniejsz obraz 5× przy użyciu INTER_AREA .
# b. Sprawdź, jak zmienia się jakość w porównaniu do innych metod.

import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = cv2.resize(image,(w//5,h//5), interpolation=cv2.INTER_AREA)
    resized1 = cv2.resize(image,(w//5,h//5), interpolation=cv2.INTER_LINEAR)
    resized2 = cv2.resize(image,(w//5,h//5), interpolation=cv2.INTER_CUBIC)
    resized3 = imutils.resize(image,height=h//5)


    cv2.imshow("resized", resized)
    cv2.imshow("resized1", resized1)
    cv2.imshow("resized2", resized2)
    cv2.imshow("resized3", resized3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")