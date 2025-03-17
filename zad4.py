# 4. Zamiana wartości piksela na czarny
# a. Pobierz od użytkownika współrzędne (x, y) .
# b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
# wychodzą poza wymiar zdjęcia.
# c. Ustaw piksel w tym miejscu na czarny (0, 0, 0) .

import cv2

image = cv2.imread("layla.png")

if image is not None:
   
    (h,w) = image.shape[:2]

    x= None
    while True:
        if x is None:
            x = int(input(f"Wprowadz wartosc X (0-{w-1})"))
            if x < 0 or x >= w:
                print("Wprowadz wartosc jeszcze raz.")
                x=None
                continue
        y = int(input(f"Wprowadz wartosc Y (0-{h-1})"))
        if y < 0 or y >= h:
            print("Wprowadz wartosc jeszcze raz.")
            continue
        image[y,x] = (0,0,0)
        print(f"ustawiono czarny kolor na wspolrzednych ({x},{y})")
        break

else:
    print("nie udalo sie wczytac obrazu")