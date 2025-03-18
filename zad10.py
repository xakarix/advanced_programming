# 10. Zmiana rozmiaru i zapis pliku
# a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku
# resized_output.jpg .

import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = imutils.resize(image,width=800)
    cv2.imwrite("resized_output.jpg", resized)
else:
    print("Bład")