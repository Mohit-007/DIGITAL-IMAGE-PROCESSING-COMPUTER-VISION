import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'C:\\Users\\RAMESHWAR LAL JI\\OneDrive\\Desktop\\IMAGE\\video.avi'
    cap = cv2.VideoCapture(filename) # reading the written video
    
    
    while (cap.isOpened()):     # if capture start 
    
        ret, frame = cap.read()     # ret = true and frame will have the tuple
        
     #   print(ret)
        
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()    
    cap.release()

if __name__ == "__main__":
    main()