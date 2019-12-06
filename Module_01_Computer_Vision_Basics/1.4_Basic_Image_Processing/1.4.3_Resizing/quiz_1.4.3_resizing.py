import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="Image you want to process.")
ap.add_argument('-w', "--width", required=True, help="Width of the image you want to resize to.")
ap.add_argument('-x', "--x_pixel", required=True, help="The x Pixel you want to find.")
ap.add_argument('-y', "--y_pixel", required=True, help="The y Pixel you want to find.")
args = vars(ap.parse_args())

print('Image:', args['image'])
print('Width:', args['width'])
print('X Pixel:', args['x_pixel'])
print('Y Pixel:', args['y_pixel'])

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

resized = imutils.resize(image, width=image.shape[1] * 2)
(b, g, r) = resized[int(args['y_pixel']), int(args['x_pixel'])]
print("Pixel at (int(args['y_pixel']), int(args['x_pixel'])) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)