# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:58:03 2018

@author: satya
"""
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

def main():
    
    w = 800
    h = 600
    
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while ret:
        
        
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        
        # Yellow Object
        low = np.array([20, 100, 100])
        high = np.array([30, 255, 255])
        
        hsv = cv2.inRange(hsv, low, high)
        
       # grey = cv2.cvtColor(d, cv2.COLOR_HSV2GRAY)
        
        blur = cv2.GaussianBlur(hsv, (9, 9), 0)
        
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
    
        dilated = cv2.dilate(th, np.ones((9, 9), np.uint8), iterations=2 )
        
        eroded = cv2.erode(dilated, np.ones((9, 9), np.uint8), iterations=2 )
        
        c = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cnts = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
     
    	  # only proceed if at least one contour was found
        if len(c) > 0:
            
    		# find the largest contour in the mask, then use
    		# it to compute the minimum enclosing circle and
    		# centroid
            #(x, y, radius) = cv2.minEnclosingCircle(c)
            #M = cv2.moments(c)
            #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            #if radius > 10:
            if 10>1:
                    #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    #cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    cv2.drawContours(frame1, c, -1, (255, 0, 0), 2)
                    cv2.imshow("Output", frame1)
            
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()