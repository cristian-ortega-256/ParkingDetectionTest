import cv2
import numpy as np
from helper import mirrorImage
from siftMatcher import drawMatchingPoints,getMatchingDescriptors,getSiftFeatures,sortMatchesByDistance

# Initialize the video capturing
cap = cv2.VideoCapture(0)

# initialize the img of the tracking object
img = cv2.imread('../assets/pinguino.jpeg',cv2.IMREAD_GRAYSCALE)
# Get keypoints & descriptors of the tracking object
kp, des = getSiftFeatures(img)

while True:
	ret, frame = cap.read()

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Get keypoints & descriptors of the actual frame
	frameKp, frameDes = getSiftFeatures(frame)

	# Get matching points sorted by acurracy
	matches = getMatchingDescriptors(des,frameDes)
	matches = sortMatchesByDistance(matches)

	frame = drawMatchingPoints(img,kp,frame,frameKp,matches)

	frame = mirrorImage(frame)
	cv2.imshow("frame", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break


img1 = cv2.imread("the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("img", img1)

cap.release()
cv2.destroyAllWindows()