# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:29:08 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import matplotlib.pyplot as plt

def main():
    # it will start the video and capture it 
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():          # if capture start then
        ret, frame = cap.read()     # return variable (boolean) and frame (image tuple) read capture variable 
        print(ret)      # true 
        print(frame)    # it will print the image tuple
    else:
       ret = False
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    #  it will show the image
    
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    # it will release the video capture
    cap.release()

if __name__ == "__main__":
    main()