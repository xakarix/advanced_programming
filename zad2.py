# 2. Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów.

import cv2

image = cv2.imread("layla.png")

#wysokosc, szerokosc, kanaly
(h,w,c) = image.shape[:3]
#same kanaly
c2 = image.shape[2]


print(f"height: {h}px")
print(f"width: {w}px")
print(f"channels: {c}px")
print(f"channels: {c2}px")