# 5. Dynamiczne przesunięcie na podstawie parametrów użytkownika
# a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
# poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
# b. Sprawdź, jak działa przesunięcie dla różnych wartości.

import numpy as np
import cv2
import imutils

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    x, y = map(int, input("Wpisz wartosc x i y oddzielone spacja: ").split())
    print(f"Wartosc X: {x}, wartosc Y: {y}")

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", image)

    shifted = imutils.translate(image, x, y)

    cv2.namedWindow("Update", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Update", 800,800)
    cv2.imshow("Update", shifted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



else:
    print("Błąd")