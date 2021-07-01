# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:11:59 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

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
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()

    # it will tell frequency of color or number of time a color in each pixel value 0 - 255

if __name__ == "__main__":
    main()