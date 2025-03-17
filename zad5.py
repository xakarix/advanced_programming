# Otwórz dwa obrazy jednocześnie w osobnych oknach. Upewnij się, że można
# je zamknąć niezależnie.

import cv2

image = cv2.imread("layla.png")
image_gray = cv2.imread("layla_gray.png")

if image is not None and image_gray is not None:
    print("zdjecia zostaly zaladowane")

    cv2.namedWindow("Zdjecie kolorowe", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Zdjecie kolorowe", 800, 800)
    cv2.namedWindow("Zdjecie w szarosciach", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Zdjecie w szarosciach", 800, 800)

    cv2.imshow("Zdjecie kolorowe", image)
    cv2.imshow("Zdjecie w szarosciach", image_gray)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("nie udalo sie wczytac zdjec")