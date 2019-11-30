import argparse
import cv2
import imutils
from datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="Image you want to process.")

args = vars(ap.parse_args())
print('Image:', args['image'])

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# what if we wanted to adjust the height of the image? We can apply
# the same concept, again keeping in mind the aspect ratio, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# of course, calculating the ratio each and every time we want to resize
# an image is a real pain -- let's create a  function where we can specify
# our target width or height, and have it take care of the rest for us.
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

# construct the list of interpolation methods
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 3x using the current interpolation
    # method
    start = datetime.now()
    resized = imutils.resize(image, width=image.shape[1] * 5, inter=method)
    end = datetime.now()
    conversion_time = end - start
    print("Method: {} took seconds: {}".format(name, conversion_time))
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
