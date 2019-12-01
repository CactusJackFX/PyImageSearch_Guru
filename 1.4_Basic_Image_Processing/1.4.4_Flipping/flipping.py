import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="Image you want to process.")
args = vars(ap.parse_args())

print('Image:', args['image'])

image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)