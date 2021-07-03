# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:56:16 2019

@author: RAMESHWAR LAL JI
"""

import cv2

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    print('Width : ' + str(cap.get(3)))  # the 3rd attribute of capture will give width
    print('Height : ' + str(cap.get(4))) # the 4th attribute of capture will give height
    
    cap.set(3, 5000)            # new resolution of width
    cap.set(4, 5000)            # new resolution of height
    
    ''' note : the resolution will decrease and frame rate will be low'''
    
    print('Width : ' + str(cap.get(3)))
    print('Height : ' + str(cap.get(4)))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Gray", output)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    

    cap.release()

if __name__ == "__main__":
    main()