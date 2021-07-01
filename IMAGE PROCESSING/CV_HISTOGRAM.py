# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:11:22 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"

    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # it will take image then col (channel r | g | b) then range of intensity
    
    red_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    green_hist = cv2.calcHist([img], [1], None, [256], [0, 255])
    blue_hist = cv2.calcHist([img], [2], None, [256], [0, 255])
    
    plt.subplot(3, 1, 1)
    plt.xlim([0, 255])
    plt.plot(red_hist, color='r')
    plt.title('Red Histogram')

    plt.subplot(3, 1, 2)
    plt.xlim([0, 255])
    plt.plot(green_hist, color='g')
    plt.title('Green Histogram')

    plt.subplot(3, 1, 3)
    plt.xlim([0, 255])
    plt.plot(blue_hist, color='b')
    plt.title('Blue Histogram')    
    
    plt.show()

if __name__ == "__main__":
    main()