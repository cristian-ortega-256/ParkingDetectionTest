import cv2

class MovementDetector:
	# Initialise the movement detection with 2 initial frames
	def __init__(self,firstFrame,secondFrame):
		self.olderFrame = firstFrame
		self.middleFrame = secondFrame

	def detectMovement(self,newFrame):
		# Calculates the diff between the three last frames
		diff = self.diffImg(self.olderFrame,self.middleFrame,newFrame)
		# Updates the frames
		self.olderFrame = self.middleFrame
		self.middleFrame = newFrame
		return diff

	def diffImg(self, t0, t1, t2):
		d1 = cv2.absdiff(t2, t1)
		d2 = cv2.absdiff(t1, t0)
		return cv2.bitwise_and(d1, d2)
