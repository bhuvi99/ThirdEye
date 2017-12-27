#For Live Video from Webcams
import cv2
import os
import numpy as np
import sys
recognizer=cv2.createLBPHFaceRecognizer()
recognizer.load("TrainData.yml")# loading Trained Data
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

test = cv2.imread(imageName,cv2.IMREAD_GRAYSCALE)#converting to gray scale
faces=faceCascade.detectMultiScale(test)
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)
i=0
lab=[]
cap=cv2.VideoCapture(0)#Video cam id

while(True):
	ret,frame=cap.read()
	#test=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	test = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(test)
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
