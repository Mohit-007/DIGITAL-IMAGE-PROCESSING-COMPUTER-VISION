# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:55:42 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_gray_512.tif"


    img = cv2.imread(imgpath1, 1)
    
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    th = 127
    max_val = 255
    
    # threshold will take variable image , threshold value , max value , algorithm 
    # binary => if pixel < threshold then low else high
    # inverse binary => ! binary
    # zero => if pixel < threshold then low else retain
    # inverse zero => if pixel > threshold then high else retain
    
    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO)
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV)
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC)
    
    output = [img, o1, o2, o3, o4, o5]
    
    titles = ['Original', 'Binary', 'Binary Inv',
              'Zero', 'Zero Inv', 'Trunc']
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()