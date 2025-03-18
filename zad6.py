# 6. Kopiowanie i wklejanie fragmentu obrazu
# a. Przytnij określony fragment obrazu (np. o wymiarach 100x100 pikseli).
# b. Wklej ten fragment w inne miejsce na obrazie.


import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]

    sliced = image[h//2:h//2+1000, w//2:w//2+1000]    

    image[800:1800,200:1200] = sliced

    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")