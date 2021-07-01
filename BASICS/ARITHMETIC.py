# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:49:55 2019

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
    
    print(img1)
    print(img1.size)
    
    
    
    X = [[[50]*3]*512]*512
    
    for i in range(512):
        for j in range(512):
            for k in range(3):
                img1[i][j][k] = img1[i][j][k] + X[i][j][k] 

    print(img1)
    cv2.imshow('hello',img1)
    
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

    
    '''
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    add = img1 + img2   
    sub = img1 - img2  
    mult = img1 * img2
    div = img1 / img2
    '''
    
    '''
    add = img + 50
    sub = img - 50
    mult = img * 1.5
    div = img / 1.5
    '''
    
    # note : img1 - img2 != img2 - img1
    '''
    titles = ['Liquid Drop', 'Lena', 'Addition', 'img1 - img2', 'img2 - img1']
    images = [img1, img2, add, sub, mult, div]
    
    print()
    
    for i in range(6):
        plt.subplot(1, 5, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 '''
 
    
if __name__ == "__main__":
    main()
    
    