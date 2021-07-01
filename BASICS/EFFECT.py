# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:52:32 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
    imgpath2 =  path + "mandril_color.tif"
   
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
  
    # write BGR2RGB if apply matlab plotting library
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    # 
    
    alpha = 0.5
    beta = 0.5
    gamma = 0
    
    # it will compute like img*alpha + img*beta + gamma => blending effect
    # it will show the image in equal proportion 
    # if alpha increase then proportion of image increases
    
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    titles = ['Liquid Drop', 'Lena', 'Weighted Addition']
    images = [img1, img2, output]
    
    print()
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()