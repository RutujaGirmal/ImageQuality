import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rock_Climbing_Color.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
m, n, ch = img.shape

matrix_trans = np.float32([[1, 0, 100], [0, 1, 50]])
translated_img = cv2.warpAffine(img, matrix_trans, (m, n))

cv2.imshow("Translated image", translated_img)
cv2.waitKey(0)