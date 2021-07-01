# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:36:24 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"

    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    # get 1+1 point and get the affine transformation
    
    point1 = np.float32([[100, 100], [300, 100], [100, 300]])
    point2 = np.float32([[200, 150], [400, 150], [200, 400]])
    
    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()

if __name__ == "__main__":
    main()