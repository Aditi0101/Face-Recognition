from webcam import Webcam
import numpy as np
import cv2

#constants
crop_pad = 20;
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# set up classes
webcam = Webcam()
webcam.start()

while True:
	img = webcam.get_current_frame()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('gray',gray) 
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	print faces
	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    cv2.imshow('gray',gray)
	    img_crop = img[y-crop_pad:y+h+crop_pad, x-crop_pad:x+w+crop_pad]
	    cv2.imshow('croped',img_crop)
	cv2.waitKey(100)
cv2.destroyAllWindows()


