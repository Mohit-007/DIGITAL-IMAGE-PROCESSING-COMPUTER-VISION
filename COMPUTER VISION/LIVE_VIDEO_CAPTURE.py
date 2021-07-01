# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:55:04 2020

@author: RAMESHWAR LAL JI
"""

# LIVE VIDEO CAPTURE  
  
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
