#Will Create resized images in the current working directory
import cv2
import os
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")# using frontalface haracascade file
with open("csv.txt") as fp:
	for l in fp:
		k=l.split(";")
		path=k[0];
		j=k[1].split("\n")
		label=j[0]
		temp= path[path.rfind("/")+1:]
		if not os.path.exists(temp[0:6]):
			os.makedirs(temp[0:6])
		img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
		faces=faceCascade.detectMultiScale(img,1.3,5)
		for(x,y,w,h) in faces:
			 resize=cv2.resize(img[y:y+h,x:x+w],(90,90))
			 cv2.imwrite(temp[0:6]+"/"+temp,resize)
