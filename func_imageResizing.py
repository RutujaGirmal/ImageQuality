import cv2
import numpy as np
import matplotlib.pyplot as plt

def decimate(img, factor):
    m,n,ch = img.shape
    x1 = int(np.ceil(m/factor))
    x2 = int(np.ceil(n/factor))
    # output = np.zeros((x1,x2,ch))
    output =[]
    for i in range(0,m,factor):
        for j in range(0,n,factor):
            output.append(img[i,j,:])

    ot = np.reshape(output,(x1,x2,ch))
    return ot

img = cv2.imread("Rock_Climbing_Color.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
dec_img = decimate(img, 5)

plt.imshow(dec_img)
plt.show()
cv2.waitKey(0)
