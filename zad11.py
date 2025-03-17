# 11. Znajdowanie najjaśniejszego piksela w obrazie
# a. Przeszukaj cały obraz i znajdź piksel o najwyższej wartości jasności.
# b. Wyświetl jego współrzędne i wartość.


import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread("layla.png")

if image is not None:

    (h,w) = image.shape[:2]

    brightness_px = -1
    px_coords = (0, 0)

    for y in range(h):
        for x in range(w):
            (b,g,r) = image[y,x]
            brightness = (b+g+r) // 3

            if brightness > brightness_px:
                brightness_px = brightness
                px_coords = (x,y)

    (b,g,r) = image[px_coords[1], px_coords[0]]
    print(f"Najjasniejszy px ma wspolrzedne (x: {px_coords[0]},y: {px_coords[1]}) i ma jansosc: {brightness_px}")
    print(f"R: {r} G: {g} B: {b}")


else:
    print("Nie udało się wczytać obrazu.")
