# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:43:59 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
 
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    # it will translate type transformation matrix
    # T = np.float([[1,0,50],[0,1,-50]])
    # print(T)
    
    # mark the origin of image (col/2 and row/2) and rotation angle + scaling of x and y 
    R = cv2.getRotationMatrix2D((columns/2, rows/2), 360, 1)  
    print(R)
    
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    
    
    plt.imshow(output)
    # plt.title('Shifted Image')
    plt.title('Rotated Image')
    plt.show()

if __name__ == "__main__":
    main()