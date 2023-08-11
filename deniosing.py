import numpy as np
import cv2
import matplotlib.pyplot as plt


##Original Image
img = cv2.imread('Building_SaltPepNoise.tif',0)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.show()
cv2.waitKey(0)

## Median Filtered Image
m,n = img.shape
img_med = np.zeros((m,n), dtype = np.int16)
for i in range(1,m-1):
    for j in range(1,n-1):
        temp = [img[i-1,j-1],img[i-1,j],img[i-1,j+1],img[i,j-1],img[i,j],img[i,j+1],img[i+1,j-1],img[i+1,j],img[i+1,j+1]]
        temp.sort()
        img_med[i,j] = temp[4]

plt.imshow(img_med,cmap='gray')
plt.title("Median Filtered Image")
plt.show()
cv2.waitKey(0)

## Cross shaped 4x4 - Median Filtered Image  - the best method to preserve edges
m,n = img.shape
img_cross4 = np.zeros((m,n), dtype = np.int16)

for i in range(2,m-2):
    for j in range(2,n-2):
        temp_cross4 = [img[i-2,j],img[i-1,j],img[i,j-2],img[i,j-1],img[i,j],img[i,j+1],img[i,j+2],img[i+1,j],img[i+2,j]]
        temp_cross4.sort()
        img_cross4[i,j] = temp_cross4[4]

plt.imshow(img_cross4,cmap='gray')
plt.title("Cross shaped 4x4 - Median Filtered Image")
plt.show()
cv2.waitKey(0)

## Cross shaped 2x2 - Median Filtered Image
m,n = img.shape
img_cross2 = np.zeros((m,n), dtype = np.int16)

for i in range(1,m-1):
    for j in range(1,n-1):
        temp_cross2 = [img[i-1,j],img[i,j-1],img[i,j],img[i,j+1],img[i+1,j]]
        temp_cross2.sort()
        img_cross2[i,j] = temp_cross2[3]

plt.imshow(img_cross2,cmap='gray')
plt.title("Cross shaped 2x2 - Median Filtered Image")
plt.show()
cv2.waitKey(0)