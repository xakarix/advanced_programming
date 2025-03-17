# 6. Obrót bez przycinania ( rotate_bound )
# a. Wykorzystaj imutils.rotate_bound , aby obrócić obraz o -33 stopnie i uniknąć
# przycięcia.
# b. Wyświetl wynik.

import argparse
import imutils
import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2, h//2)

    rotated = imutils.rotate_bound(image, -33)

    cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Photo", 800,800)
    cv2.imshow("Photo", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Błąd")