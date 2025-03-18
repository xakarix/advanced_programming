# 5. Zastosowanie odbicia na wybranym obszarze
# a. Wczytaj obraz i wytnij z niego fragment (np. środek obrazu lub prawą
# połowę).
# b. Odbij tylko wycięty fragment i wklej go z powrotem do obrazu.

import cv2

image = cv2.imread("layla.png")

if image is not None:
    (h,w) = image.shape[:2]
    (cX,cY) = (w//2,h//2)

    rh = image[:,cX:]
    flipped = cv2.flip(rh,1)
    image[:,cX:] = flipped
    
    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Blad")