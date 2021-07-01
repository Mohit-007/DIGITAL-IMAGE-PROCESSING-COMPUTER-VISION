# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:30:20 2020

@author: RAMESHWAR LAL JI
"""

# MATLAB PLOTTING LIBRARY

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
