# 5. Eksperymentowanie z pętlą
# a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
# kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
# poprzedniego i mieć środek w tym samym miejscu.

import numpy as np
import cv2

canvas = np.zeros((400,400, 3), dtype="uint8")

(cX,cY) = (canvas.shape[1]//2, canvas.shape[0]//2)
blue=(255,0,0)

for r in range(0,400,20):
    tl = (cX - r // 2, cY - r //2)
    br = (cX + r // 2, cY + r //2)
    cv2.rectangle(canvas,tl,br,blue)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
