# 5. Kolorowanie fragmentu obrazu
# a. Podziel obraz na 4 równe części (ćwiartki).
# b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
# c. Wyświetl obraz po zmianach.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    (cX,cY) = (w//2, h//2)

    #cwiartki
    tl = image[0:cY, 0:cX]
    tr = image[0:cY, cX:w]
    bl = image[cY:h, 0:cX]
    br = image[cY:h, cX:w]

    # cv2.imshow("TL", tl)
    # cv2.imshow("TR", tr)
    # cv2.imshow("BL", bl)
    # cv2.imshow("BR", br)

    image[0:cY, 0:cX] = (255,0,0)

    cv2.namedWindow("Updated", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Updated", 800,800)
    cv2.imshow("Updated", image)



    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("nie udalo sie wczytac obrazu")