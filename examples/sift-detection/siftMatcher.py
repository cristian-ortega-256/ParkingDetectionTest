import cv2
import numpy as np

def getSiftFeatures(img):
	# SIFT Detector
	sift = cv2.xfeatures2d.SIFT_create()
	# SIFT Detection key points
	kp, des = sift.detectAndCompute(img,None)
	return kp,des

def getMatchingDescriptors(des1,des2):
	# Brute force matching
	bf = cv2.BFMatcher(cv2.NORM_L2,crossCheck=True)
	# Match descriptors.
	matches = bf.match(des1,des2)
	return matches

def drawMatchingPoints(img1,kp1,img2,kp2,matches):
	# Drawing 
	return cv2.drawMatches(img1,kp1,img2,kp2,matches[:20], None, flags=2)
	
def sortMatchesByDistance(matches):
	return sorted(matches, key = lambda x:x.distance)