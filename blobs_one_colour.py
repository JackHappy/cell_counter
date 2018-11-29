#source: https://github.com/jagracar/OpenCV-python-tests/blob/master/OpenCV-tutorials/imageProcessing/colorSpaces.py


import numpy as np
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get the next frame
    ret, frame = cap.read()

    # Convert from BGR scale to HSV scale
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue mask
    lowerBlue = np.array([0,0,130])
    upperBlue = np.array([178,255,255])
    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lowerBlue, upperBlue)
    
    # OR Brown mask
    lower_brown = np.array([0,70,0])          #(red->,      white->,   black->)
    upper_brown = np.array([50,255,255])      #(->purple,   ->colour,  ->colour)
    mask = cv2.inRange(hsv, lower_brown, upper_brown)





    # Remove everything that is not in the mask
    res = cv2.bitwise_and(frame, frame, mask=mask)
   

    # Display all the difference images
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('neg_res', -res)
    k = cv2.waitKey(5) & 0xFF
    
    # User interaction
    if k == 27:
        break

# When everything is done, release the capture and close all windows
cap.release()
cv2.destroyAllWindows()