import cv2
import os
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getId():
	l=0
	try:
		l=input("Enter ID:")
		print "Ok"
		return l
	except:
		print "Kindly enter 6 Digit Numerical ID:"
		try:
			l=input("Enter ID:")
			print "Ok"
			return l
		except:
			print "Kindly enter 6 Digit Numerical ID:"
			return getId()
def getData():
			
	l=getId()
	path="/home/suryathri/ThirdEye/Data/"+str(l) # path where collected faces from webcam will be saved in separate ID Folder
	if not os.path.exists(path):
		os.makedirs(path)
	else:
		print "Already Exists"
		getData()
	cap = cv2.VideoCapture(0)#webcam id :0
	i=1
	path=path+"/"
	while i<101:
		ret, frame = cap.read()	
		test = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(test)
		for(x,y,w,h) in faces:
			path1=path+str(l)+"_"+str(i)+".jpg"		
			cv2.imwrite(path1,frame)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.imshow("capture",frame)
			cv2.waitKey(1)		
		print i		
		i=i+1
	print "Done"
	cv2.destroyAllWindows()
getData()
