def compute_thresh(img, thresh, delta_T):
    [x_low, y_low] = np.where(img<=thresh)
    [x_high, y_high] = np.where(img>thresh)

    m1 = np.mean(img[x_low, y_low])
    m2 = np.mean(img[x_high, y_high])

    new_thresh = (m1+m2)/2

    if abs(thresh-new_thresh) < delta_T:
        return new_thresh
    else:
        return compute_thresh(img, new_thresh, delta_T)


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Plane.jpg", cv2.IMREAD_GRAYSCALE)

T = compute_thresh(img, 30, 1)

ret, thresh_img = cv2.threshold(img, T, 255, cv2.THRESH_BINARY)
output = cv2.hconcat([img, thresh_img])
cv2.imshow("threshold", output)
cv2.waitKey(0)







































# def thres_finder(img, thres,delta_T):
    
#     # Step-2: Divide the images in two parts
#     x_low, y_low = np.where(img<=thres)
#     x_high, y_high = np.where(img>thres)
    
#     # Step-3: Find the mean of two parts
#     mean_low = np.mean(img[x_low,y_low])
#     mean_high = np.mean(img[x_high,y_high])
    
#     # Step-4: Calculate the new threshold
#     new_thres = (mean_low + mean_high)/2
    
#     # Step-5: Stopping criteria, otherwise iterate
#     if abs(new_thres-thres)< delta_T:
#         return new_thres
#     else:
#         return thres_finder(img, thres=new_thres,delta_T=1.0)

# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread("Plane.jpg",cv2.IMREAD_GRAYSCALE)
# vv1 = thres_finder(img, 30, 1.0)
# # threshold the image
# ret, thresh = cv2.threshold(img,vv1,255,cv2.THRESH_BINARY)
# # Display the image side by side
# out = cv2.hconcat([img,thresh])
# cv2.imshow('threshold',out)
# cv2.waitKey(0)