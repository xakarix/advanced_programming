# 3. Odbicie względem obu osi
# a. Odbij obraz zarówno poziomo, jak i pionowo (czyli względem obu osi).

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    flipped = cv2.flip(image,-1)

    cv2.imshow("Photo", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Blad")