# 3. Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów.

import cv2

image_gray = cv2.imread("layla.png", cv2.IMREAD_GRAYSCALE)

# c = image_gray.shape[2]

#zmiana okna na większe
cv2.namedWindow("Obraz w szarosciach", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Obraz w szarosciach", 1200, 1200)


# print(f"liczba kanałów: {c}")

cv2.imshow("Obraz w szarosciach", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows