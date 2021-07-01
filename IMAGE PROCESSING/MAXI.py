# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:00:53 2019

@author: RAMESHWAR LAL JI
"""

import cv2
import numpy as np

def main():
    
    # it will set the height and width of frame
    
    w = 800
    h = 600
    
    # it will capture the frame
    
    cap = cv2.VideoCapture(0)
    
    
    cap.set(3, w)
    cap.set(4, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    # if frame opened then ret = true else false
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    # it will open 1+1 frame
    # 1 will be normal and 2 to detect the motion
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    # if true (frame opened)
    
    while ret:
        
        # absolute difference will make contour will be stored in frame d
        
        d = cv2.absdiff(frame1, frame2)     
        
        # it will trasform the image (difference) in gray scale
        
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        
        #
        
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        
        # it will get the threshold by binary algorithm
        
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
    
        # it will diate thereshold image
        
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=1 )
        
        # it will erode the dialated image
        
        eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )
        
        # it will draw contour on the base of eroded image
        
        c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame1, c, -1, (0, 0, 255), 2)

        cv2.imshow("Original", frame2)
        cv2.imshow("Output", frame1)
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()