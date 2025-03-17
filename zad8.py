# 8. Modyfikacja całego wiersza pikseli
# a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony (0, 255, 0) .
# b. Wyświetl obraz przed i po zmianie.


import cv2

image = cv2.imread("layla.png")

if image is not None:

    (h,w) = image.shape[:2]

    image[99, :] = (0, 255, 0)
   
    cv2.namedWindow("Updated", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Updated", 800,800)
    cv2.imshow("Updated", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("nie udalo sie wczytac obrazu")