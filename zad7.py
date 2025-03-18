# 7. Podział obrazu na siatkę
# a. Podziel obraz na 9 równych części (3x3).
# b. Wyświetl wszystkie części osobno.

import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]

    v_slice = h//3
    h_slice = w//3

    s1 = image[0:v_slice, 0:h_slice]
    s2 = image[0:v_slice, h_slice:2*h_slice]
    s3 = image[0:v_slice, 2*h_slice: w]

    s4 = image[v_slice: 2*v_slice, 0:h_slice]
    s5 = image[v_slice: 2*v_slice, h_slice:2*h_slice]
    s6 = image[v_slice: 2*v_slice, 2*h_slice: w]
    
    s7 = image[2*v_slice:h, 0:h_slice]
    s8 = image[2*v_slice:h, h_slice: 2*h_slice]
    s9 = image[2*v_slice:h, 2*h_slice:w]
    

    cv2.imshow("Piece 1", s1)
    cv2.imshow("Piece 2", s2)
    cv2.imshow("Piece 3", s3)
    cv2.imshow("Piece 4", s4)
    cv2.imshow("Piece 5", s5)
    cv2.imshow("Piece 6", s6)
    cv2.imshow("Piece 7", s7)
    cv2.imshow("Piece 8", s8)
    cv2.imshow("Piece 9", s9)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")