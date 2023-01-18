import cv2
import numpy as np
import imutils

#Reading the video
vidcap = cv2.VideoCapture('fifa2018.mp4')
# sucess, image = vidcap.read()
count = 0
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("images/frame"+str(count)+".jpg", image)
    return hasFrames

sec = 2
frameRate = 2
count = 88

success= getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

cv2.imshow(vidcap)
cv2.waitKey(8)
# success = True

# idx = 0
#
# #Read the video frame by frame
# while success:

    #converting into hsv image
    # hsv = cv2.cvtColor (image, cv2. COLOR_BGR2HSV)
    # #green range
    # lower_green = np.array([40,40, 40])
    # upper_green = np.array([70,255, 255])
    #
    # #blue range
    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])
    #
    # #Red range
    # lower_red = np.array([0, 0, 0])
    # upper_red = np.array([0, 0, 255])
    #
    # #define a mask ranging from lower to upper
    # mask = cv2.inRange(hsv, lower_green, upper_green)
    # #Do masking
    # res = cv2.bitwise_and(image, image, mask=mask)
    # #convert to hsv to gray
    # res_bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    # res_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

