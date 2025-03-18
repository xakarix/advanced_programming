# 4. Porównanie różnych metod interpolacji
# a. Powiększ obraz 3× przh użyciu różnych metod interpolacji ( INTER_NEAREST ,
# INTER_LINEAR , INTER_CUBIC , INTER_LANCZOS4 ).
# b. Wyświetl i porównaj wyniki.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]

    resized = cv2.resize(image,(w*3,h*3), interpolation=cv2.INTER_NEAREST)
    resized1 = cv2.resize(image,(w*3,h*3), interpolation=cv2.INTER_LINEAR)
    resized2 = cv2.resize(image,(w*3,h*3), interpolation=cv2.INTER_CUBIC)
    resized3 = cv2.resize(image,(w*3,h*3), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow("resized", resized)
    cv2.imshow("resized1", resized1)
    cv2.imshow("resized2", resized2)
    cv2.imshow("resized3", resized3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Bład")