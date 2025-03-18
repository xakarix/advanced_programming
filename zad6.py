# 6. Odbicie na podstawie wyboru użytkownika
# a. Napisz skrypt, który wczytuje obraz i pyta użytkownika o sposób odbicia
# ( 0 – pionowe, 1 – poziome, -1 – oba).
# b. Na podstawie wyboru wykonuje operację i wyświetla wynik.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    while True:
        try:
            x = int(input("podaj sposob odbicia: 0 – pionowe, 1 – poziome, -1 – oba: "))

            if x not in [-1,0,1]:
                print("niewlasciwa wartosc")
            else:
                break
        except ValueError:
            print("niepoprawny typ")
    
    flipped = cv2.flip(image,x)
    
    cv2.imshow("Photo", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Blad")