# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:30:43 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
    imgpath2 =  path + "mandril_color.tif"
    
    img = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    img3 = abs(255-img1)
    img4 = abs(255-img2)

    
    titles = ['Color Image', 'Grayscale', 'Color-Negative', 'Grayscale-Negative']
    images = [img1, img2, img3, img4]
    
    print()
    
    # note : for gray scale image color map must be gray
    
    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 2)
    plt.imshow(images[1], cmap='gray')
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 3)
    plt.imshow(images[2])
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 4)
    plt.imshow(images[3], cmap='gray')
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()