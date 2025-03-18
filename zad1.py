# 1. Odbicie poziome
# a. Wczytaj obraz i wykonaj odbicie lustrzane w poziomie.
# b. Wyświetl wynik.


import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    flipped = cv2.flip(image,1)

    cv2.imshow("Photo", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Blad")