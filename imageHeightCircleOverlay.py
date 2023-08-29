import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def imageHtCircleOverlay(img,imgHeight_factor):
    imgHeight_factor = imgHeight_factor/100
    [m,n,ch] = img.shape
    # Image Center
    centerx = n/2
    centery = m/2 
    # Compute radius
    r = imgHeight_factor*(math.sqrt(math.pow(centerx,2) + math.pow(centery,2)))
    th = np.arange(0,1+2*math.pi,math.pi/50)
    # Calculate co-ordinates for each sample
    xcenter = r*np.cos(th) + centerx
    ycenter = r*np.sin(th) + centery
    return xcenter,ycenter


# Load the Image
img = cv2.imread("BW_noisy.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Take user input for desired Image height estimation - 0% center to 100% edge of Image
imgHeight_factor = int(input("Enter the image height: "))
# Call function imageHt
[xcenter, ycenter] = imageHtCircleOverlay(img,imgHeight_factor)
# Plot the Image Height circle over image
plt.imshow(img)
plt.plot(xcenter,ycenter)
plt.show()
cv2.waitKey(0)
