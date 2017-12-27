import cv2
import os
import numpy as np
import sys
recognizer=cv2.createLBPHFaceRecognizer()
recognizer.load("TrainData.yml")# loading Trained Data
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
imageName=sys.argv[1] # geting input image name through commandline
test = cv2.imread(imageName,cv2.IMREAD_GRAYSCALE)#converting to gray scale
faces=faceCascade.detectMultiScale(test)
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)
i=0
lab=[]
for(x,y,w,h) in faces:		
	if(w>80 and h>80):
		predicted_label,confidence=recognizer.predict(test[y:y+h,x:x+w])
		if  confidence<100:		
			
			lab.append(predicted_label)
			#cv2.rectangle(test,(x,y),(x+w,y+h),(255,255,255),2)
			#cv2.cv.PutText(cv2.cv.fromarray(test),result,(x,y+h),font,255);
lab.sort()
lines=[]
file=open("FindLabel.txt","r+")# correspoinding names for the labels is saved in FindLabel.txt
k=file.read()
j=k.split("\n")
file=open("Result.txt",'w')
for x in lab:
	file.write(j[x]+","+"\n") #Result Will Be Saved In Result.txt file
	#print j[x]+","
cv2.imwrite("Result.jpg",test)
