# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:20:49 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\misc\\"

    imgpath1 =  path + "5.1.12.tiff"
    img = cv2.imread(imgpath1, 0)
    
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # note : for very little difference of foreground and background it is ! good 
    # note : apply adaptive threshold method (it is good to detect edges of image)
    # note : it will take block size and constant with the algorithm and image with range 
    
    
    block_size = 13 # ( block size % 2 == 1 (odd) and it must never equal 1)
    constant = 2
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    th2 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
    
    output = [img, th1, th2]
    
    titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()