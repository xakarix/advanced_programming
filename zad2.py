# 2. Rysowanie prostokątów, utwórz czarny obraz o wymiarach 400x400 pikseli i
# narysuj na nim:
# a. Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
# b. Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.

import cv2
import numpy as np

canvas = np.zeros((400,400,3), dtype="uint8")

green = (0,255,0)
red = (0,0,255)

cv2.rectangle(canvas,(0,0), (100,50), green)
cv2.rectangle(canvas,(255,280), (400,400), red, 3)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()