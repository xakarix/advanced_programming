# 4. Dynamiczny wybór ROI
# a. Napisz skrypt, który pozwala użytkownikowi podać wartości startX , endX ,
# startY , endY z klawiatury.
# b. Przytnij obraz zgodnie z wprowadzonymi wartościami i wyświetl wynik.


import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    while True:
        try:
            startX, endX = map(int, input("Podaj wartosc startX, endX oddzielajac je spacja: ").split())
            if startX < 0 or endX > w or startX >= endX:
                print("podano zle wartosci")
                continue

            startY, endY = map(int, input("Podaj wartosc startY, endY oddzielajac je spacja: ").split())
            if startY < 0 or endY > h or startY >= endY:
                print("podano zle wartosci")
                continue
            
            break

        except ValueError:
            print("Podano inny znak")

            

    sliced = image[startY:endY, startX:endX]

    cv2.imshow("Photo", sliced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")