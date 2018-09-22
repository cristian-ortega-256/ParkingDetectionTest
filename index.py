import sys
import cv2
import numpy as np
from Video import Video
from MovementDetector import MovementDetector
from ImageTransformators import toGrayScale

webcam =  Video()

firstFrame = toGrayScale(webcam.getFrame())
secondFrame = toGrayScale(webcam.getFrame())
movementDetector = MovementDetector(firstFrame,secondFrame)

while True:
	actualFrame = toGrayScale(webcam.getFrame())
	cv2.imshow("Frame",movementDetector.detectMovement(actualFrame))

	key = cv2.waitKey(1)
	if key == 27:
		break

webcam.release()
cv2.destroyAllWindows()