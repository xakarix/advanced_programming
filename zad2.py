# 2. Symulacja efektu "przepalenia" obrazu
# a. Dodaj do każdego piksela wartość 150, ale używając NumPy.
# b. Porównaj wynik z operacją cv2.add() .

import cv2
import numpy as np

image = cv2.imread("layla.png")

if image is not None:
    M = np.ones(image.shape, dtype="uint8") * 150
    
    added_cv2 = cv2.add(image,M)
    added_np = image + M


    cv2.imshow("Photo cv2", added_cv2)
    cv2.imshow("Photo np", added_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")