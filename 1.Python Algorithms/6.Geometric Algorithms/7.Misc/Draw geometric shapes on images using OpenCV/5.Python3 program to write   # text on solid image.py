# Python3 program to write
# text on solid image
import numpy as np
import cv2

# Creating a black image with 3
# channels RGB and unsigned int datatype
img = np.zeros((400, 400, 3), dtype = "uint8")

# writing text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'GeeksForGeeks', (50, 50),
			font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('dark', img)

# Allows us to see image
# untill closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
