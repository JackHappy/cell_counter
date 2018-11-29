import numpy as np
import cv2
import matplotlib.pyplot as plt

# for live feed
cap = cv2.VideoCapture(0)
# For processing a still image
#cap = cv2.imread('messi5.jpg',0)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read() 

    # Our operations on the frame come here
    #colour = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # From https://resources.oreilly.com/examples/9781785283840/blob/7d51d357875a18be16e015c527b81f07973128c8/Learning_OpenCV_3_Computer_Vision_with_Python_Second_Edition_Code/Chapter%205_Code/watershed.py
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]

    #plt.imshow(img)
    plt.show()




    # Display the resulting frame
    cv2.imshow('frame',img)
    
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    # if spacebar
    if key == ord(chr(32)):
        original = frame
        break
    
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()