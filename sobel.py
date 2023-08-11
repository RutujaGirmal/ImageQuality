import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rock_Climbing_Luma.jpg", cv2.IMREAD_GRAYSCALE)
## SOBEL FILTER (horizontal)- harsh on edges
sob_filt = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) * (1/4)
print(sob_filt)

m,n = img.shape
output_sob = np.zeros((m,n), dtype=np.int16)
for i in range(1,m-1):
    for j in range(1,n-1):
        temp1 = img[i-1,j-1]*sob_filt[0,0] +img[i-1,j]*sob_filt[0,1] +img[i-1,j+1]*sob_filt[0,2] +img[i,j-1]*sob_filt[1,0] +img[i,j]*sob_filt[1,1] +img[i,j+1]*sob_filt[1,2] +img[i+1,j-1]*sob_filt[2,0] +img[i+1,j]*sob_filt[2,1] +img[i+1,j+1]*sob_filt[2,2] 
        output_sob[i,j]=temp1

plt.imshow(output_sob,cmap='gray')
plt.show()
cv2.waitKey(0)

## PREWITT FILTER (horizontal) - better edge smoothening
prev_filt = np.array([[-1,-1,-1],[0,0,0],[1,1,1]]) * (1/3)
print(prev_filt)

output_prev = np.zeros((m,n), dtype=np.int16)
for i in range(1,m-1):
    for j in range(1,n-1):
        temp2 = img[i-1,j-1]*prev_filt[0,0] +img[i-1,j]*prev_filt[0,1] +img[i-1,j+1]*prev_filt[0,2] +img[i,j-1]*prev_filt[1,0] +img[i,j]*prev_filt[1,1] +img[i,j+1]*prev_filt[1,2] +img[i+1,j-1]*prev_filt[2,0] +img[i+1,j]*prev_filt[2,1] +img[i+1,j+1]*prev_filt[2,2] 
        output_prev[i,j]=temp2

plt.imshow(output_prev,cmap='gray')
plt.show()
cv2.waitKey(0)

## LAPLACIAN - 2nd derivative method
lap_filt = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
print(lap_filt)

output_lap = np.zeros((m,n), dtype=np.int16)
for i in range(1,m-1):
    for j in range(1,n-1):
        temp3 = img[i-1,j-1]*lap_filt[0,0] +img[i-1,j]*lap_filt[0,1] +img[i-1,j+1]*lap_filt[0,2] +img[i,j-1]*lap_filt[1,0] +img[i,j]*lap_filt[1,1] +img[i,j+1]*lap_filt[1,2] +img[i+1,j-1]*lap_filt[2,0] +img[i+1,j]*lap_filt[2,1] +img[i+1,j+1]*lap_filt[2,2] 
        output_lap[i,j]=temp3

plt.imshow(output_lap,cmap='gray')
plt.show()
cv2.waitKey(0)

