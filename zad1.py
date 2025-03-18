# 1. Wybór ROI na podstawie współrzędnych
# a. Zdefiniuj ROI, który obejmuje lewy górny róg obrazu o wymiarach 100x100
# pikseli.
# b. Wyświetl wynik.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    roi = image[0:100, 0:100]

    cv2.imshow("Photo", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")