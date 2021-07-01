# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:14:20 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\"
    
    imgpath =  path + "lena_color_512.tif"



    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # it is a technique that will decrese the memory size of image
    # it will tone down image or shade will decrease
    
    # reshape the image to apply k means cluster
    
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    
    # it will get max iteration and criteria with numerical value
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    # number of color will be equal to k (no. of minimum shades)
    
    K=2
   
    # it will take reshape , no. of shade , criteria , algorithm
    
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # it will return k centers and resolution will have get alue by flattning the label
    # resolution array will tell intesity of color on the pixel in k color shade
    # get output by resolution and reshape it in image 
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img.shape))
    
    
    K=4
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output2 = res1.reshape((img.shape))
    
    K=12
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img.shape))

    output = [img, output1, output2, output3]
    titles = ['Original Image', 'K=2', 'K=4', 'K=12']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()