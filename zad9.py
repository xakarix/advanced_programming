# 9. Zmiana wartości pikseli w określonym zakresie
# a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255) .
# b. Wyświetl obraz przed i po zmianie.


import cv2

image = cv2.imread("layla.png")

if image is not None:
   
    image[50:100, 50:100] = (255,255,255)

    cv2.namedWindow("Updated", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Updated", 800,800)
    cv2.imshow("Updated", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("nie udalo sie wczytac obrazu")