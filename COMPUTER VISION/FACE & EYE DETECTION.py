
# FACE DETECTION

import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\RAMESHWAR LAL JI\\DATA SCIENCE A-Z\\COMPUTER VISION APPLICATION\\DETECTION FILE\\haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')

# detector = dlib.get_frontal_face_detector()

'''
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        hi, wi = face.right(), face.bottom()
        cv2.rectangle(frame, (x,y), (hi, wi), (0, 0 , 255), 2)
        
        
    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



'''

cap = cv2.VideoCapture(0)

# it will help to dectect face connecting phone camera with laptop
# address = "http://[2401:4900:4640:30a6:bf0c:449e:3055:691]:8080/video"
# cap.open(address)
while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    i = 0

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        i = i+1
        cv2.putText(img, 'face' + str(i), (x-12, y-12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
    # display output    
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''

# EYE DETECTION

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture('C:\\Users\\RAMESHWAR LAL JI\\OneDrive\\Desktop\\Movies\\Horror\\CV\\MEDIA\\video.avi')

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

'''