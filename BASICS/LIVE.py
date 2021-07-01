# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:42:29 2019

@author: RAMESHWAR LAL JI
"""
# 25 frame per second

import cv2

def main():
    windowName = "Live Video Feed"   # title of the window
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)        # video capture  
    
    if cap.isOpened():               # if capture video start 
        ret, frame = cap.read()      
    else:
        ret = False

    while ret:                      # while it will be true
    
        ret, frame = cap.read()         # read the capture
        
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # processing the video
        
        cv2.imshow("Gray", output)          # it will show the variation of output
        cv2.imshow(windowName, frame)       # it will show the window frame
        if cv2.waitKey(1) == 27:            # if escape key then exit the loop
            break

    cv2.destroyAllWindows()         # destroy all the window

    cap.release()                   # release the capture

if __name__ == "__main__":
    main()