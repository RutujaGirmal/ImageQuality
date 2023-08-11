from cmath import log10
import numpy as np
import cv2
from matplotlib import pyplot as plt

cc_image = cv2.imread("CC.png")
cc_image = (cv2.cvtColor(cc_image, cv2.COLOR_RGB2BGR)).astype(np.uint8)
plt.imshow(cc_image)
plt.show()
cv2.waitKey(0)
# cc_image = cc_image/cc_image.max()
## ROI selection and SNR

# r = cv2.selectROI(cc_image)
# print(r)
# selected_roi = cc_image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
# plt.imshow(selected_roi)
# plt.show()
# cv2.waitKey(0)

# snr_num = np.mean(r)
# snr_den = np.std(r)
# snr = snr_num/snr_den
# print("The SNR for selected patch is", snr)
# print("SNR in dB", 20*log10(snr))

m, n, ch = cc_image.shape

## Adding Gaussian Noise

mean = 1
var = 0.4
sigma = var**0.5
gauss = (np.random.normal(mean, var, (m, n, ch))).astype(np.uint8)
gauss = gauss.reshape(m, n, ch)

noisy_image = cc_image + gauss
plt.imshow(noisy_image)
plt.show()
cv2.waitKey(0)
rg = cv2.selectROI(noisy_image)
snr_num = np.mean(rg)
snr_den = np.std(rg)
snr = snr_num/snr_den
print("The SNR for selected patch is (GaussianNoise)", snr)
print("SNR in dB", 20*log10(snr))

## Adding Speckle noise

gauss = np.random.randn(m, n, ch).astype(np.uint8)
gauss = gauss.reshape(m, n, ch)
gauss.max()
noisy_image = (cc_image + cc_image*gauss).astype(np.uint8)
plt.imshow(noisy_image)
plt.show()
cv2.waitKey(0)
rg = cv2.selectROI(noisy_image)
snr_num = np.mean(rg)
snr_den = np.std(rg)
snr = snr_num/snr_den
print("The SNR for selected patch is (SpeckleNoise)", snr)
print("SNR in dB", 20*log10(snr))
