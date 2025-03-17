# 1. Odczyt wartości piksela
# a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym
# rogu (współrzędne 0,0 ).
# b. Wyświetl wartości składowych koloru (R, G, B).

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    # (b,g,r) = image[3050,3621]
    (b,g,r) = image[0,0]
    print(f"Pixel at (0,0) - Red: {r}, Green: {g}, Blue {b}")

    cv2.namedWindow("Kot", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Kot", 800,800)
    cv2.imshow("Kot", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("nie udalo sie wczytac obrazu")


