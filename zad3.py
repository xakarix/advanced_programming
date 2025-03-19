# 3. Przyciemnianie obrazu
# a. Zmniejsz jasność obrazu o 80 jednostek.
# b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.


import cv2
import numpy as np

image = cv2.imread("layla.png")

if image is not None:
    M = np.ones(image.shape, dtype="uint8") * 80
    
    added_cv2 = cv2.subtract(image,M)
    added_np = image - M


    cv2.imshow("Photo cv2", added_cv2)
    cv2.imshow("Photo np", added_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")