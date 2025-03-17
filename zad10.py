# 10. Obrót w pętli
# a. Wykonaj pętlę, która obraca obraz co 15 stopni od 0 do 360 i wyświetla
# każdą wersję na ekranie.
# b. Dodaj opóźnienie cv2.waitKey(500) , aby obserwować zmiany.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    for r in range(0,360,15):
        rotated = imutils.rotate(image, -r)
        cv2.imshow("Update", rotated)
        cv2.resizeWindow("Update", 800,800)
        cv2.waitKey(500)




    # cv2.destroyAllWindows()

else:
    print("Błąd")