import numpy as np
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
nice_number = 1
old_to_new_raio = 0.50 # 0.10 is fast, 0.90 is slow
all_blobs_count_smooth = 0
brown_blobs_count_smooth = 0


def watershed_and_count(frame):
    # Accepts a BGR frame, returns the frame with markers
    # Also returns object count
    img = frame
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)


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

    #**UPDATE** CODE BROKEN HERE
    
    #thresholding a color image, here keeping only the blue in the image
    th=cv2.inRange(img,(255,0,0),(255,0,0)).astype(np.uint8)


    #inverting the image so components become 255 seperated by 0 borders.
    th=cv2.bitwise_not(th)

    #calling connectedComponentswithStats to get the size of each component
    nb_comp,output,sizes,centroids=cv2.connectedComponentsWithStats(th,connectivity=4)

    #taking away the background
    nb_comp-=1; sizes=sizes[0:,-1]; centroids=centroids[1:,:]

    annotated_image = img
    object_count = nb_comp

    return annotated_image, object_count

def smooth_my_number(old_number, new_number):
    smoothed = old_to_new_raio * old_number + (1-old_to_new_raio) * new_number

    return smoothed

while(True):
    # Capture frame-by-frame (doing this for each colour now (may streamline later))
    # ret, img = cap.read()
    
    # All blobs
    ret, all_blobs_img = cap.read()
    all_blobs_img, all_blobs_count = watershed_and_count(all_blobs_img)
    all_blobs_img_RGB = cv2.cvtColor(all_blobs_img, cv2.COLOR_BGR2RGB)
    all_blobs_count_smooth = smooth_my_number(all_blobs_count_smooth,all_blobs_count)
    all_blobs_string = "Total blob count is: " + str(int(all_blobs_count_smooth))
    cv2.putText(all_blobs_img, all_blobs_string, (20,20), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), thickness=1)

    # Brown blobs
    ret, brown_blobs_img = cap.read()
    brown_blobs_hsv = cv2.cvtColor(brown_blobs_img, cv2.COLOR_BGR2HSV)
    lower_brown = np.array([0,70,0])          
    upper_brown = np.array([50,255,255])   
    brown_mask = cv2.inRange(brown_blobs_hsv, lower_brown, upper_brown)

    # Remove everything that is not in the mask
    brown_blobs_img = cv2.bitwise_and(brown_blobs_img, brown_blobs_img, mask=brown_mask)
    brown_blobs_img_to_process = cv2.cvtColor(brown_blobs_img,cv2.COLOR_HSV2BGR)
    brown_blobs_img_processed, brown_blobs_count = watershed_and_count(brown_blobs_img_to_process)

    brown_blobs_count_smooth = smooth_my_number(brown_blobs_count_smooth,brown_blobs_count)
    brown_blobs_string = "Brown blob count is: " + str(int(brown_blobs_count_smooth))
    cv2.putText(brown_blobs_img, brown_blobs_string, (20,20), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), thickness=1)

    ###########################################DISPLAY######################################################
    # Display the resulting frame
    cv2.imshow('all blobs',all_blobs_img_RGB)
    cv2.imshow('brown blobs',brown_blobs_img_processed)
    cv2.imshow('brown_mask',brown_mask)
    
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    # if spacebar
    if key == ord(chr(32)):
        original = frame
        break
    if key == ord('s'):
        bins = list(range(np.amax(sizes)))
        #plot distribution of your cell sizes.
    
        numbers = sorted(sizes)
        plt.hist(sizes,numbers)
        plt.show()
        print(f'The \n\nnm_comp is {nb_comp}, \n\noutput {output},\n\nsizes{sizes},\n\ncentroids{centroids}')
    
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()