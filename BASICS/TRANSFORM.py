# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:16:47 2019

@author: RAMESHWAR LAL JI
"""
#  it will tell all the color

'''
import cv2

def main():
    j = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j =  j +1

    print('There are ' + str((j+1)) + ' color conversion flags in OpenCV.')
 
if __name__ == "__main__":
    main()
    
'''    



import cv2
import matplotlib.pyplot as plt

def main():
    
    img = cv2.imread("C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif",1)

    # it will variate or transform the color by 1 color space into new color space

    img0 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.title('Color Image BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
    
    plt.imshow(img0)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
if __name__ == "__main__":
    main()