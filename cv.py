import cv2

im_in = cv2.imread("test.jpg")

cv2.imshow("Show Image",im_in)

cv2.waitkey(0)

cv2.destroyAllWindows()

cv2.imwrite("test2.jpg",im_in)