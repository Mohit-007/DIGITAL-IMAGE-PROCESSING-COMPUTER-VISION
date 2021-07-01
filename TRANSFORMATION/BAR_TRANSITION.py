# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:11:31 2019

@author: RAMESHWAR LAL JI
"""

import cv2

def emptyFunction():
    pass

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
    imgpath2 =  path + "mandril_color.tif"

    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    
    
    windowName = "Transition Demo"
    cv2.namedWindow(windowName)
    
    # it will create a track bar for pass value 0 and thousand to vary alpha and beta
    cv2.createTrackbar('Alpha', windowName, 0, 1000, emptyFunction)
    
    while(True):
        
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 1000
        beta = 1 - alpha
        
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        
    #    print (alpha, beta)
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()