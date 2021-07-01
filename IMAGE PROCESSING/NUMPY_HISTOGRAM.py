# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:08:05 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"

    img = cv2.imread(imgpath, 0)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    hist, bins = np.histogram(img.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist)
    plt.title('Histogram')
    plt.show()

if __name__ == "__main__":
    main()