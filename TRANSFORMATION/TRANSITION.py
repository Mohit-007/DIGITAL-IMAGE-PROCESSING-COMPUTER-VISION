# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:04:37 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import numpy as np
import time
#import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath1 =  path + "lena_color_512.tif"
    imgpath2 =  path + "mandril_color.tif"

    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    ''' it will variate alpha and beta value with a sleep of time '''
    
    for i in np.linspace(0, 1, 100):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow('Transition', output)
        time.sleep(0.02)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()