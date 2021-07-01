# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:44:12 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"
    
#    imgpath1 =  path + "4.2.07.tiff"

    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#    th = 0
#    max_val = 255
   
#    ret, binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )

#    k = np.ones((5, 5), np.uint8)

#    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
    
    erosion = cv2.erode(img, k, iterations = 5)
    
    dilation = cv2.dilate(img, k, iterations = 5)
    
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
    
    # note : apply dialation on a image and erosion on the dialated = gradient of image
    # note : apply erosion on a image and dialation on the eroded = gradient of image
    
    print(k)
    
    output = [img, erosion, dilation, gradient]
    
    titles = ['Original', 'Erosion', 'Dilation', 'Gradient']
    
    # note : gradient = erosion - dilation
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()