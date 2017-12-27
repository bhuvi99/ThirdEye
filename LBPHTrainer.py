import cv2
import os
import numpy as np
import sys
# arg1=sys.argv[1]
#recognizer=cv2.createFisherFaceRecognizer() #For Using Fisher Faces Algoritham
#recognizer=cv2.createEigenFaceRecognizer() # For Using Eigen Face Algoritham
recognizer=cv2.createLBPHFaceRecognizer()
#img=cv2.imread("opencvlogo.png",cv2.IMREAD_GRAYSCALE)
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
#faces=faceCascade.detectMultiScale(img);
#path="/home/rgukt/Desktop/FACES/DA"
#image_paths = [os.path.join(path, f) for f in os.listdir(path)]
#print image_paths
images=[]
labels=[]
count=0
with open('csv.txt') as fp:
    for line in fp:
        #print line
        k=line.split(";")
        j=k[1].split("\n")
	img=cv2.imread(k[0],cv2.IMREAD_GRAYSCALE);
	print "On Going..."
	nbr=int(j[0])
	faces=faceCascade.detectMultiScale(img)
	for (x,y,w,h) in faces:
		images.append(img[y: y + h, x: x + w])
           	labels.append(nbr)

recognizer.train(images,np.array(labels)) # Traing LBPH Face recognizer
recognizer.save("TrainData.yml")# Traing Data Will Be Saved in Data.yml file
