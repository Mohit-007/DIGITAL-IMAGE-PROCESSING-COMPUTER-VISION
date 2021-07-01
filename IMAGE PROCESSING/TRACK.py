# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:05:09 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import numpy as np

def main():

    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'C:\\Users\\RAMESHWAR LAL JI\\OneDrive\\Desktop\\IMAGE\\video.avi'
    cap = cv2.VideoCapture(filename) # reading the written video
        
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
       ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   # it will transform bgr => hsv

        # range of color help to trak it
        
        # Blue Color
#        low = np.array([100, 50, 50])
#        high = np.array([140, 255, 255])

        # Green Color
#        low = np.array([40, 50, 50])
#        high = np.array([80, 255, 255])

        # Red Color
#        low = np.array([140, 150, 0])
#        high = np.array([180, 255, 255])

        # Color
#        low = np.array([155, 155, 155])
#        high = np.array([255, 255, 255])

        
        image_mask = cv2.inRange(hsv, low, high)  # it will check the range and make mask around and in range
        
        output = cv2.bitwise_and(frame, frame, mask = image_mask) # it will bitwise and the frame and get the color of mask range
        
        cv2.imshow("Image mask", image_mask)
       # print(img_mask)   # check the value of different position of pixel and intensity of color
        cv2.imshow("Original Webcam Feed", frame)
        cv2.imshow("Color Tracking", output)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()