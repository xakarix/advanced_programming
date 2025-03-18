# 9. Zapis przyciętego obrazu
# a. Przytnij obraz do obszaru o wymiarach 300x300 pikseli.
# b. Zapisz wynik jako nowy plik cropped_image.jpg .

import cv2

image = cv2.imread("avatar.jpg")

if image is not None:
    (h,w) = image.shape[:2]

    roi = image[3000:3300, 1200:1500]
    
    cv2.imwrite("cropped_image.jpg", roi)
else:
    print("error")