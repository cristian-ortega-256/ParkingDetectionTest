import cv2
import numpy as np

class Video:
	# Initialize with the integrated webcam for default
	def __init__(self,source=0):
		self.cap = cv2.VideoCapture(0)

	def read(self):
		return self.cap.read()
		
	def getFrame(self):
		return self.cap.read()[1]
	
	def release(self):
		self.cap.release()