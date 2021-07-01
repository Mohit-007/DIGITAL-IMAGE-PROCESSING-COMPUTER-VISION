# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:19:31 2019

@author: RAMESHWAR LAL JI
"""

import cv2

def main():
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)           # it capture the video
    
    # address of the storage location
    filename = 'C:\\Users\\RAMESHWAR LAL JI\\OneDrive\\Desktop\\IMAGE\\video.avi'
    
    # it will be applied for coding and decoding
    
    
    codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')      # encoding mode
    framerate = 30                                          # frame resolution
    resolution = (640, 480)                                 # resolution 
    
   # note : if resolution decrease then frame rate increases
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution) # it will write video in video file output
    
    # it read and write
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
      #  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        VideoFileOutput.write(frame) # it will write the frame in the video file output
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

if __name__ == "__main__":
    main()