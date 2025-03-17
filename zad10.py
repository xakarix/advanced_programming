# 10. Sprawdzenie różnicy wartości pikseli
# a. Pobierz wartości pikseli w dwóch różnych miejscach obrazu i porównaj je
# (np. (50,50) i (200,200) ).
# b. Wypisz różnice w wartościach R, G, B.


import cv2

image = cv2.imread("layla.png")

if image is not None:
    
    (b, g, r) = image[2020, 2020]  
    print(f"Piksel w punkcie (2020, 2020): R: {r}, G: {g}, B: {b}")

    (b2, g2, r2) = image[3080, 3080]
    print(f"Piksel w punkcie (3080, 3080): R: {r2}, G: {g2}, B: {b2}")

    diff_r = abs(r - r2)
    diff_g = abs(g - g2)
    diff_b = abs(b - b2)

    print(f"Różnice w wartościach: R: {diff_r}, G: {diff_g}, B: {diff_b}")

else:
    print("nie udalo sie wczytac obrazu")