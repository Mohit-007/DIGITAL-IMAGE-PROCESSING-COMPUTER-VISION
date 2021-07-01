# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:37:04 2020

@author: RAMESHWAR LAL JI
"""
'''
	const char* fileName;
	if(argc != 2){
	
		fileName = "./lena_color.tif";
	}
	else
		fileName = argv[1];

	// Load Image
	Mat image = imread(fileName,  IMREAD_UNCHANGED);

	if(image.empty()){
	
		cout << "Can't load image." << endl;
		return -1;
	}

	int height = image.rows;
	int width = image.cols;


	// Create new images
	Mat grayScaleImage, binaryImage, smallImage;
	
	int key;

	//convert colored image to gray scale
	cvtColor(image, grayScaleImage, COLOR_BGR2GRAY);

	// binarize the grayscale image
	threshold(grayScaleImage, binaryImage, 128, 255, THRESH_BINARY);

	// resize image
	resize(image, smallImage, Size(), 0.5, 0.5, INTER_LINEAR);
//	resize(image, smallImage, Size(width/2, height/2), INTER_LINEAR);

	//display original image
	namedWindow("image",CV_WINDOW_AUTOSIZE);
	imshow("image", image);

	cout << "Press \n 'i' to display original image \n 'g' for grayscale \n 'b' for binary, \n 's' for smaller sized image and 'Esc' to exit" << endl;

	while(1)
	{
		//wait for keyboard input
		key = waitKey(0);
		

		// press 'Esc' to quit the program
		if(key == 27)
			break;

		switch(key)
		{
			// 'i' pressed, display the original image
			case 'i':
				imshow("image", image);
				break;

			// 'g' pressed, display the grayscale image
			case 'g':
				imshow("image", grayScaleImage);
				break;

			// 'b' pressed, display the binarized image
			case 'b':
				imshow("image", binaryImage);
				break;
			// 's' pressed, display the resized smaller image
			case 's':
				imshow("image", smallImage);
				break;

		}
	}

	//free memory
 	destroyWindow("image");


'''
import cv2
import numpy as np




def main():

    '''
    
    # it is variable to store the image path
    imgpath = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif"
    
    # it will read the image (1 == grayscale image) and store it in img variable
    img = cv2.imread(imgpath,1)
    
    # it is variable (name of the window that will show the image)
    windowName = 'MyWindow'
    
    # it will create the window with window name
    cv2.namedWindow(windowName)
    
    # it will show the image in the window
    cv2.imshow("MyWindow",img)
    
    # it is waiting for the event of the keyboard
    k = cv2.waitKey(0)
    
    # note : 27 (key code of escape) if it is applied (escape event ) then 
    if k == 27:
        # it will destroy all the windows
        cv2.destroyAllWindows()
    # it will write or show the image in ipython console    
    cv2.imwrite(imgpath,img)
    
    '''
    
    # it is variable to store the image path
    imgpath = "C:\\Users\\RAMESHWAR LAL JI\\Downloads\\standard_test_images\\standard_test_images\\lena_color_256.tif"
    
    # it will read the image (1 == grayscale image) and store it in img variable
    img = cv2.imread(imgpath,1)
   
    # it is threshold value variable
    th = 128
    # it is max value
    max_val = 255

    # it is library to convert the image from bgr to gray
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # it will resize the image 
    # it will decrease the image half horizontally
    # it will increase the image 1.5 vertically
    # it can have many method like
    # 
    img_resize = cv2.resize( img, None, fx=0.5, fy=1.5, interpolation=cv2.INTER_LINEAR )
    ret, img_binary = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
    
    
    while(1):
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows()
        elif key == 111:    
            cv2.imshow('original',img)
        elif key == 103:
            cv2.imshow('gray',img_gray)
        else:
            print(key)
        
            

        
     
        

if __name__ == "__main__":
    main()