# 2. Modyfikacja pojedynczego piksela
# a. Zmień kolor piksela w prawym dolnym rogu obrazu na czerwony (0, 0, 255) .
# b. Wyświetl obraz przed i po zmianie.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    (b,g,r) = image[h-1,w-1]
    print(f"R: {r}, G: {g}, B: {b}")
    cv2.namedWindow("Kot", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Kot", 800,800)
    cv2.imshow("Kot", image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    image[h-1,w-1] = (0,0,255)

    (b,g,r) = image[h-1,w-1]
    print(f"R: {r}, G: {g}, B: {b}")

    cv2.namedWindow("Kot po zmianie", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Kot po zmianie", 800,800)
    cv2.imshow("Kot po zmianie", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("nie udalo sie wczytac obrazu")