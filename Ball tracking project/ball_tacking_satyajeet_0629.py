import cv2
import numpy as np
import time
import imutils
import argparse
from collections import deque

#setup cam
cap = cv2.VideoCapture(0)
time.sleep(2)

if True: # Setup SimpleBlobDetector parameters.
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

if True: # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)

if True: #setup trail
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--buffer", type=int, default=64)
    args = vars(ap.parse_args())
    pts = deque(maxlen=args["buffer"])

if True: # Finding the focal length of the camera using a manually entered parameters

    known_dist = 30 #cm
    known_dia = 7 #cm
    obs_dia = 125 #px

    # focal length for this camera
    focal_len = (obs_dia * known_dist)/known_dia

    t0 = time.time()
    t1 = 0
    x1 = 0
    y1 = 0
    z1 = 0
    zd=0
    center = None

while True:

    # frame stores current capture
    ret, frame = cap.read()

    # frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yellow Ball colors
    low = np.array([15, 100, 50])
    high = np.array([35, 255, 255])

    # Tracking by color
    mask = cv2.inRange(hsv, low, high)

    # median blur
    mask = cv2.medianBlur(mask,15)

    # erode noise
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel,iterations = 1)

    # invert mask
    mask = 255-mask

    # Detect blobs.
    keypoints = detector.detect(mask)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Draw the centres as green small circles
    frame_with_keypoints = cv2.drawKeypoints(frame_with_keypoints, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    
    #trace trail
    for i in range (1, len(pts)):
        if pts[i] is None or pts[i-1] is None:
            continue
        else:
            thickness = 1
            cv2.line(frame_with_keypoints,pts[i-1],pts[i],(255,0,0), thickness)

    # Show blobs
    cv2.imshow("Keypoints", frame_with_keypoints)

    '''
    # Plot the red circles and green centres on the mask as well and the show the mask
    mask_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    mask_with_keypoints = cv2.drawKeypoints(mask_with_keypoints, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    cv2.imshow("Mask Keypoints", mask_with_keypoints)
    '''

    center = None
    
    if keypoints: # If we have found a ball! Then show gui with the values
        x = keypoints[0].pt[0]
        y = keypoints[0].pt[1]
        s = keypoints[0].size
        z = (focal_len * known_dia)/s
        
        t = time.time() - t0 # update t
        td = t - t1
        zd = z - z1
        if zd<30 or zd==z:
            
            v = np.sqrt([(zd)*(zd)])/td
            print('X = ', int(x), '\tY = ', int(y), '\tZ = ', int(z), 'cm\tTime = ', t, 's\tinst. Vel in z = ', v, 'cm/s')
            center = (int(x),int(y))
            pts.appendleft(center)
            x1=x
            y1=y
            z1=z
            t1=t

    if cv2.waitKey(50) == 27: # Press Esc to break loop
        break

cap.release()
cv2.destroyAllWindows()

