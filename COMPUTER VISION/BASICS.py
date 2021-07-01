# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:18:13 2019

@author: RAMESHWAR LAL JI
"""

# OPENCV

import cv2

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()
  
 
    
