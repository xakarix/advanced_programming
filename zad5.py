# 5. Kadrowanie twarzy
# a. Znajdź zdjęcie z twarzą.
# b. Znajdź obszar, w którym się znajduje, i przytnij obraz tak, aby pozostała
# tylko twarz.


import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]

    roi = image[h//2 - 1000: h//2 +1700, w//2 - 1200: w//2 + 1200]
    
    cv2.imshow("Photo", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")