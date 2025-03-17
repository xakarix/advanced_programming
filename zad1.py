# 1. Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się
# stanie, gdy podasz błędną ścieżkę.

import cv2

image = cv2.imread("layla.png")
# image = cv2.imread("layla1.png")

if image is None:
    print("Błąd, nie można odczytać zdjęcia!")
else:
    print("Zdjęcie zostało wczytane poprawnie.")