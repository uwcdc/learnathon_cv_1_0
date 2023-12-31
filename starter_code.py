# Import the necessary packages
import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and show some basic information on it
image = cv2.imread(args["image"])
print("width: {w} pixels".format(w=image.shape[1]))
print("height: {h}  pixels".format(h=image.shape[0]))
print("channels: {c}".format(c=image.shape[2]))

# Show the image and wait for a keypress
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# Save the image -- OpenCV handles converting filetypes automatically
cv2.imwrite("newimage.jpg", image)
