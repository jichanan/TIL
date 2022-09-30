from cv2 import IMREAD_UNCHANGED
import numpy as np
import cv2

ff = np.fromfile('ㅋㅋ.jpg', np.uint8)
img = cv2.imdecode(ff, IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1, fy=1.0, interpolation=cv2.INTER_LINEAR)

cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.9)

cv2.imshow('cartoon_view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()