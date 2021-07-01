# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:32:10 2020

@author: RAMESHWAR LAL JI
"""

# IMAGE GRADIENT AND EDGE DETECTION

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
#lap = np.uint8(np.abs(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


