# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:19:50 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"

    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)
    
    output1 = cv2.merge((output1_R, output1_G, output1_B))

#    clahe = cv2.createCLAHE()
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    output2_R = clahe.apply(R)
    output2_G = clahe.apply(G)
    output2_B = clahe.apply(B)
    
    output2 = cv2.merge((output2_R, output2_G, output2_B))


    output = [img, output1, output2]
    titles = ['Original Image', 'Adjusted Histogram', 'CLAHE']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()