# 3. Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
# narysuj na nim:
# a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
# b. Czerwony okrąg o promieniu 60 px w środku obrazu.

import cv2
import numpy as np

canvas = np.zeros((300,300,3), dtype="uint8")

(cX,cY) = canvas.shape[1]//2, canvas.shape[0]//2

blue=(255,0,0)
red=(0,0,255)

cv2.circle(canvas,(40,40), 40, blue)
cv2.circle(canvas,(cX,cY), 60, red)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
