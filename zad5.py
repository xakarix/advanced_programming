# 5. Zastosowanie arytmetyki do detekcji zmian w obrazach
# a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami (np.obiekt przesunięty).
# b. Oblicz ich różnicę ( cv2.absdiff(image1, image2) ).
# c. Zinterpretuj wynik – jakie zmiany są widoczne?

import cv2
import numpy as np
import imutils

image = cv2.imread("layla.png")

if image is not None:
    image2 = cv2.flip(image, 1) 
    diff = cv2.absdiff(image, image2)


    cv2.imshow("Photo", image)
    cv2.imshow("Photo2", image2)
    cv2.imshow("Diff", diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")