import cv2

def mirrorImage(img):
	return cv2.flip( img, 1 )