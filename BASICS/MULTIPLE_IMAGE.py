# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:50:00 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_256.tif"
    imgpath2 =  path + "mandril_color.tif"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
   
    '''
    
    titles = ['Liquid Drop', 'Lena']
    images = [img1, img2]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    '''
    
    # the sub plot will re organize the image in row and coloumn and define position of a image
    
    plt.subplot(1, 2, 1)
    plt.imshow(img1)
    plt.title('Liquid Drop')
    plt.xticks([])
    plt.yticks([])
    

    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.title('Lena')
    plt.xticks([])
    plt.yticks([])
    
    plt.show()  
 
if __name__ == "__main__":
    main()