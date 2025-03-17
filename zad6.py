# 6. Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
# Pobierz współrzędne środka obrazu.
# Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze
# środkiem obrazu, kolorem czerwonym (0, 0, 255) .
# Wyświetl obraz po zmianach.

import cv2

image = cv2.imread("layla.png")

if image is not None:
   
    (h,w) = image.shape[:2]
    (cX, cY) = (w//2, h//2)

    sqr = 100
    tlx_sqr = cX - (sqr // 2)
    tly_sqr = cY - (sqr // 2)

    image[tly_sqr: tly_sqr+sqr, tlx_sqr:tlx_sqr+sqr] = (0,0,255)

    cv2.namedWindow("Updated", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Updated", 800,800)
    cv2.imshow("Updated", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("nie udalo sie wczytac obrazu")