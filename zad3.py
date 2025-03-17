# 3. Znajdowanie środka obrazu
# a. Wczytaj obraz i oblicz współrzędne jego środka.
# b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    print(f"srodek obrazu ma wsporzedne: ({cX}, {cY})")

    (b,g,r) = image[cX, cY]
    print(f"R: {r}, G: {g}, B: {b}")

else:
    print("nie udalo sie wczytac obrazu")