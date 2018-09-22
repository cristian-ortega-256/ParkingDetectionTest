import cv2

def toGrayScale(frame):
	return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)