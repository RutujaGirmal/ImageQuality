from numpy import dtype, float16, int16, uint8


def Equalized_img(img):
    m,n= img.shape
    a = np.zeros([256], dtype=float16)
    b = np.zeros([256], dtype=float16)
    factor = (1/(m*n))
    for i in range(m):
        for j in range(n):
            g = img[i,j]
            a[g] = a[g] + 1

    for k in range(256):
        for l in range(k+1):
            b[k] += a[l]*factor

    b = np.round(b * 255)
    b = b.astype(uint8)
    for i in range(m):
        for j in range(n):
            g = img[i,j]
            img[i,j] = b[g]
    return img


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rock_Climbing_Color.jpg",0)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.show()
cv2.waitKey(0)
eq = Equalized_img(img)


plt.imshow(eq,cmap='gray')
plt.title("Equalized Image")
plt.show()
cv2.waitKey(0)
