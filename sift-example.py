import cv2
import numpy as np

img = cv2.imread('the_book_thief.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("me_holding_book.jpg", cv2.IMREAD_GRAYSCALE)

# SIFT Detection
sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# KeyPoints Draw
#img = cv2.drawKeypoints(img,kp1,None)
#img2 = cv2.drawKeypoints(img2,kp2,None)

# Brute force matching
bf = cv2.BFMatcher(cv2.NORM_L2,crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img,kp1,img2,kp2,matches[:50], None, flags=2)

#Image show
#cv2.imshow("Image",img)
#cv2.imshow("Image2",img2)
cv2.imshow("Image3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()