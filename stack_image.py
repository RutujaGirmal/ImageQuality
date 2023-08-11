import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("Rock_Climbing_Color.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
x_rep = int(input("Enter the repetition vertiically:"))
y_rep = int(input("Enter the repetition horizontally:"))
m, n, ch = img.shape
output_img = np.zeros((x_rep*m, y_rep*n, ch), dtype=int)
new_row = x_rep*m
new_col = y_rep*n
ver_idx=[]
for k in range(0,x_rep):
    ver_idx.append(m*k)
hor_idx=[]
for l in range(0,y_rep):
    hor_idx.append(n*l)
# for i in range(0,new_row-1):
#     for j in range(0,new_col-1):
for c1 in range(0,x_rep):
    for c2 in range(0,y_rep):
        output_img[ver_idx[c1]:m+ver_idx[c1],hor_idx[c2]:n+hor_idx[c2],:] = img[:,:,:]

print("ver idx", ver_idx)
print("hor idx", hor_idx)

plt.imshow(output_img)
plt.show()
cv2.waitKey(0)