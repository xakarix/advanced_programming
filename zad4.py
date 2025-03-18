# 4. Porównanie efektów
# a. Wyświetl cztery wersje obrazu:
# i. Oryginał
# ii. Odbicie poziome
# iii. Odbicie pionowe
# iv. Odbicie względem obu osi

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    flipped_h = cv2.flip(image,1)
    flipped_v = cv2.flip(image,0)
    flipped = cv2.flip(image,-1)

    cv2.imshow("Photo", image)
    cv2.imshow("Photo h", flipped_h)
    cv2.imshow("Photo v", flipped_v)
    cv2.imshow("Photo v and h", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Blad")