# 7. Wycięcie fragmentu obrazu
# a. Podziel obraz na 9 równych części.
# b. Pobierz fragment obrazu obejmujący środek.
# c. Wyświetl wycięty fragment osobno.

import cv2

image = cv2.imread("layla.png")

if image is not None:

    (h,w) = image.shape[:2]
    x_split = w //3
    y_split = h //3

    c_sqr = image[y_split: y_split*2, x_split: x_split*2]
   
    cv2.namedWindow("Updated", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Updated", 800,800)
    cv2.imshow("Updated", c_sqr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("nie udalo sie wczytac obrazu")