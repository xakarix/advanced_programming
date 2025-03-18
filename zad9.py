# 9. Dynamiczna zmiana rozmiaru w pętli
# a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co 20%.
# b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem ( cv2.waitKey(500) ).

import cv2
import imutils
import numpy as np

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    for r in np.arange(1.0,3.0,0.2):
        resized = imutils.resize(image, height=int(h*r))
        cv2.imshow("resized", resized)
        cv2.waitKey(500)

   
    # cv2.destroyAllWindows()
else:
    print("Bład")