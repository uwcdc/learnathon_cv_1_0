# Import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and show it
image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
cv2.imwrite("./output_images/rotation_original_image.jpg", image)

# Grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# Rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = 'write your code here'
# cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.imwrite("./output_images/rotation_rotated_by_45_degrees.jpg", rotated)

# Rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = 'write your code here'
# cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.imwrite("./output_images/rotation_rotated_by_negative_90_degrees.jpg", rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by Offset & 45 Degrees", rotated)
cv2.imwrite("./output_images/rotation_rotated_by_offset_and_45_degrees.jpg", rotated)

# Finally, let's use our helper function in imutils to rotate the image by 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
# cv2.imshow("Rotated by 180 Degrees", rotated)
# cv2.waitKey(0)
cv2.imwrite("./output_images/rotation_rotated_by_180_degrees.jpg", rotated)