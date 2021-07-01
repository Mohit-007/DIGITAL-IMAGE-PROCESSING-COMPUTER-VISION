# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:53:42 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"
    

    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # it will get the intensity value of threshold
    
    ret, thresh = cv2.threshold(gray, 75, 255, 0)
    
    # it is easy to find the boundary in gray image
    
    # it will take algorithm and threshold vallue
    # note : all color with high or low than threshold have contour around them     
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # it will have all the countour point
    
#    print(contours)
#    print(hierarchy)
    
    # color of contour and width of contour
    
    # it will draw the contour on image with respect to countour variable of a color intensity of a width
    
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    
    original = cv2.imread(imgpath, 1)
    
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    output = [original, img]
    titles = ['Original', 'Contours']
    
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()