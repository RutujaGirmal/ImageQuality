from cmath import log10
import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("BW_noisy.jpg")


image = cv2.bilateralFilter(image, 5, 75, 75)
image = image/image.max()
m, n, ch = image.shape
plt.imshow(image)
plt.show()
cv2.waitKey(0)
# f = f + beta*(f-fblur)
beta = 0.4
LP_image = cv2.blur(image, (5,5))
LP_image = LP_image/LP_image.max()
plt.imshow(LP_image)
plt.show()
cv2.waitKey(0)
sharp_image = image + (beta*(image-LP_image))
sharp_image = sharp_image/sharp_image.max()
plt.imshow(sharp_image)
plt.show()
cv2.waitKey(0)

