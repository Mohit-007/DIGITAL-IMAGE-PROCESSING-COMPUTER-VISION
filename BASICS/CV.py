
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif",0)
'''img = cv2.imread("C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif",0)'''


''' it will initialize the array pixel by zero and it will be resolution => 256*256'''
img = np.zeros((512,512,3), np.uint8)




''' note : next line will overwrite the previous line '''


''' it will draw a line with start and end coordinate  with color of line and thickness'''
cv2.line(img,(0,99),(99,0,),(255,0,0),1)
''' it will draw a rectangle with start and end coordinate  with color and thickness'''
cv2.rectangle(img,(0,0),(80,70),(0,255,0),-1)
''' it will draw a circle with center and radius of circle with color and thickness'''
cv2.circle(img, (60, 60), 50, (0, 0, 255), 1)
''' it will draw a ellipse with 1+1 center and angle of rotation of ellipse with color and thickness'''
cv2.ellipse(img, (160, 260), (50, 20), 0, 0, 360, (127, 127, 127), -1)
    
''' print point '''


'''  position of point '''
points = np.array([[80, 2], [125, 0], [179, 0], [230, 5], [30, 50]], np.int32)
''' reshape the point '''
points = points.reshape((-1, 1, 2))
''' color of point and visibility of point and joining the point '''
cv2.polylines(img, [points], True, (0, 255, 255))
    
text1 = 'MOHIT'
cv2.putText(img, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0))


''' it will give the datatype of image '''
print(img.dtype)   
''' it will give the resolution of image => (height,width,*)'''
print(img.shape)  
''' it will multiply value of the dimension '''
print(img.size)
''' the image decode in a n dimensional array '''
print(type(img))
print(img)

''' * => note gray image will not possess r , g , b color '''


cv2.imwrite("C:\\Users\\RAMESHWAR LAL JI\\OneDrive\\Desktop\\IMAGE\\lena_color_256.jpg",img)

cv2.imshow('Lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
   
   