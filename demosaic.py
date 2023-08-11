import numpy as np
import cv2
import matplotlib.pyplot as plt

def demosaic(raw_img):
    [m,n] = raw_img.shape
    output = np.array((m/2,n/2,3),dtype="int32")
    output[:,:,0] = raw_img[0:-1:2, 0:-1:2]
    output[:,:,1] = (raw_img[1:-1:2, 0:-1:2] + raw_img[0:-1:2,1:-1:2])/2
    output[:,:,2] = raw_img[1:-1:2, 1:-1:2]

    return output




raw_img = cv2.imread("parrots_mos.jpg")
opt_img = demosaic(raw_img)

plt.imshow(opt_img)
plt.show()
cv2.waitKey(0)
