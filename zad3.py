# 3. Przycięcie prawej połowy obrazu
# a. Przycięcie prawej połowy obrazu
# b. Wyświetl tylko prawą połowę.


import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    right = image[:, w//2:w]

    cv2.imshow("Photo", right)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")