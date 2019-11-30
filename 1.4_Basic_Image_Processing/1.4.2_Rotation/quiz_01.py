import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="Image you want to process.")
ap.add_argument('-r', "--rotate", required=True, help="How much you want to rotate.")
ap.add_argument('-x', "--x_pixel", required=True, help="The x Pixel you want to find.")
ap.add_argument('-y', "--y_pixel", required=True, help="The y Pixel you want to find.")
args = vars(ap.parse_args())

print('Image:', args['image'])
print('Rotate Angle:', args['rotate'])
print('X Pixel:', args['x_pixel'])
print('Y Pixel:', args['y_pixel'])

image = cv2.imread(args['image'])
cv2.imshow('Quiz 01', image)
cv2.waitKey(0)

rotated_image = imutils.rotate(image, int(args['rotate']), center=(50,50))
(b, g, r) = rotated_image[int(args['y_pixel']), int(args['x_pixel'])]
print("Pixel at (int(args['y_pixel']), int(args['x_pixel'])) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

cv2.imshow('Rotated', rotated_image)
cv2.waitKey(0)
