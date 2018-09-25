import cv2
import numpy as np

#setup cam
cap = cv2.VideoCapture(0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 50


# Filter by Area.
params.filterByArea = True
params.minArea = 50
params.maxArea = 100000
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.3

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.1
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.1

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

# Finding the focal length of the camera using a manual process

known_dist = 30 #cm
known_dia = 7 #cm
obs_dia = 125 #px

# focal length for this camera
focal_len = (obs_dia * known_dist)/known_dia

while True:
    #frame stores current capture
    ret, frame = cap.read()

    #frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Yellow Ball colors
    low = np.array([20, 100, 100])
    high = np.array([30, 255, 255])

    #Tracking by color
    mask = cv2.inRange(hsv, low, high)

    #median blur
    mask = cv2.medianBlur(mask,15)

    #erode noise
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel,iterations = 1)

    #invert mask
    mask = 255-mask

    # Detect blobs.
    keypoints = detector.detect(mask)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    frame_with_keypoints = cv2.drawKeypoints(frame_with_keypoints, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    # Show blobs
    cv2.imshow("Keypoints", frame_with_keypoints)

    mask_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    mask_with_keypoints = cv2.drawKeypoints(mask_with_keypoints, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    cv2.imshow("Mask Keypoints", mask_with_keypoints)
    

    if keypoints:
        x = keypoints[0].pt[0]
        y = keypoints[0].pt[1]
        s = keypoints[0].size
        z = (focal_len * known_dia)/s
        print('x = '+ str(x) + 'px y = '+ str(y) + 'px z = '+ str(z) + 'cm diameter = '+ str(s) + 'px')


    


    if cv2.waitKey(50) == 27:
        break




cap.release()
cv2.destroyAllWindows()