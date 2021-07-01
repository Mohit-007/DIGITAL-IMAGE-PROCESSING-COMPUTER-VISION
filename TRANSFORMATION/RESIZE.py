# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:36:10 2019

@author: RAMESHWAR LAL JI
"""

import cv2

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
    img1 = cv2.imread(imgpath1, 1)

    # fx and fy will be the dimension of image and inter method will help to improve quality
    output = cv2.resize( img1, None, fx=0.5, fy=1.5, interpolation=cv2.INTER_AREA )
   
    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()
