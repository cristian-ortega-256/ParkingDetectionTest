import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# SIFT Detection
sift = cv2.xfeatures2d.SIFT_create()

# SURF Detection
surf = cv2.xfeatures2d.SURF_create()

while True:
	ret, frame = cap.read()

	#kp, des = sift.detectAndCompute(frame,None)
	#kp, des = surf.detectAndCompute(frame,None)
	
	#frame = cv2.drawKeypoints(frame,kp,None)
	frame = cv2.flip( frame, 1 )
	cv2.imshow("frame", frame)

	
	key = cv2.waitKey(1)
	if key == 27:
		break


img1 = cv2.imread("the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("img", img1)

cap.release()
cv2.destroyAllWindows()