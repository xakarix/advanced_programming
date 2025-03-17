# 4. Zmień rozmiar okna wyświetlania obrazu tak, by dostosować je do różnych
# ekranów, np. cv2.WINDOW_NORMAL - znajdź w dokumentacji odpowiednią funkcję
# do tego.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    cv2.namedWindow("Layla", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Layla", 800, 800)

    cv2.imshow("Layla", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("nie udalo sie wczytac zdjecia")