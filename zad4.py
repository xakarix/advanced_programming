# Wczytaj obraz w skali szarości i zapisz go jako nowy plik - znajdź w
# dokumentacji odpowiednią funkcję do tego.

import cv2

image_gray = cv2.imread("layla.png", cv2.IMREAD_GRAYSCALE)

if image_gray is None:
    print("Nie udało się załadowac zdjecia")
else:
    print("Obraz został załadowany")
    cv2.imwrite("layla_gray.png", image_gray)
    print("Obraz został zapisany")
