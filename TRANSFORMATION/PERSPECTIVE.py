# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:48:49 2019

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
    
    # it is very similar to affine transformation
    
    # take point and make a rectangle
    
    point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
    point2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    
    P = cv2.getPerspectiveTransform(point1, point2)
    
    print(P)
    
    # it can take all kind of value in range of resolution instead row and coloumn
    
    output = cv2.warpPerspective(img1, P, (700, 700))
    
    
    plt.imshow(output)
    plt.title('Changed Perspective')
    plt.show()

if __name__ == "__main__":
    main()