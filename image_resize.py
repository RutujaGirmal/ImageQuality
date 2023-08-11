import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rock_Climbing_Color.jpg")
img = cv2.cvtColor(img,  cv2.COLOR_RGB2BGR)
decimator_factor = int(input("Enter the decimator factor : "))
m, n, ch = img.shape
x1 = int(np.ceil(m/decimator_factor))
y1 = int(np.ceil(n/decimator_factor))
temp =[]
for i in range(0,m,decimator_factor):
    for j in range(0,n,decimator_factor):
        temp.append(img[i,j,:])
decimated_op = np.reshape(temp,(x1,y1,ch))        
plt.imshow(decimated_op)
plt.show()
cv2.waitKey(0)