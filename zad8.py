# 8. Animacja przesuwającego się ROI
# a. Wczytaj obraz i dynamicznie przesuwaj ROI w poziomie (np. przesunięcie
# co 10 pikseli), aby stworzyć efekt „przesuwania kamery”.
# b. Wyświetlaj na ekranie kolejne wycinki ROI po kliknięciu w klawiature.

import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]

    move = 10

    for r in range(0, w-3000, move):
        roi = image[:,r:r+3000]
        cv2.imshow("Photo", roi)
        cv2.waitKey(500)

else:
    print("error")