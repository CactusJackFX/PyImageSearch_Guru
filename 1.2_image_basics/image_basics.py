import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True. help="Path to the Image.")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
cv2.show("Original", image)