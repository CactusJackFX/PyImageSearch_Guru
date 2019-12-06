# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("florida_trip.png")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
people = image[173:235, 13:81]
cv2.imshow("People", people)
cv2.waitKey(0)

# ...and now let's crop the entire body
boat = image[124:212, 225:380]
cv2.imshow("Boat", boat)
cv2.waitKey(0)


# image[124:212, 225:380]