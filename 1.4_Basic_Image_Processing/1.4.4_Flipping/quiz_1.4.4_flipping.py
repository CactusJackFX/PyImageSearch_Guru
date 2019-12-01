import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="Image you want to process.")
ap.add_argument('-r', "--flip", required=True, help="How much you want to rotate.")
ap.add_argument('-x', "--x_pixel", required=True, help="The x Pixel you want to find.")
ap.add_argument('-y', "--y_pixel", required=True, help="The y Pixel you want to find.")
args = vars(ap.parse_args())

print('Image:', args['image'])
print('Rotate Angle:', args['flip'])
print('X Pixel:', args['x_pixel'])
print('Y Pixel:', args['y_pixel'])

image = cv2.imread(args['image'])
cv2.imshow('Quiz 1.4.4', image)
cv2.waitKey(0)

flipped = cv2.flip(image, int(args['flip']))
cv2.imshow("Flipped Image", flipped)
cv2.waitKey(0)

rotated = imutils.rotate(flipped, 45)
cv2.imshow("Flipped & Rotated Image", rotated)
cv2.waitKey(0)

vertical = cv2.flip(rotated, 0)
(b, g, r) = vertical[int(args['y_pixel']), int(args['x_pixel'])]
print("Pixel at Y={y}, X={x} - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b, y=args['y_pixel'], x=args['x_pixel']))
cv2.imshow("Flipped & Rotated & Flipped Again Image", vertical)
cv2.waitKey(0)
