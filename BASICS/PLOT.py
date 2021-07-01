# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:59:55 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    img = cv2.imread("C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif",0)

    ''' all type of color map '''
    
    
    plt.imshow(img, cmap='Reds')    # plot the image in the console with x and y axis
    plt.title('Gray Colormap')      # Title of the image 
    
    # vanish the x and y axis
    plt.xticks([])              
    plt.yticks([])
    
    # show it in the console
    plt.show()
    
    
    ''' default color will be bgr => blue'''
    
    plt.imshow(img)
    plt.title('Default Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()  
 
if __name__ == "__main__":
    main()