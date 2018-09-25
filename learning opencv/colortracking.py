# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:00:56 2018

@author: satya
"""


import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Yellow Object
        low = np.array([20, 100, 100])
        high = np.array([30, 255, 255])
        
        image_mask = cv2.inRange(hsv, low, high)
        image_mask = cv2.GaussianBlur(image_mask,(5,5),0)
        
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow("Image mask", image_mask)
        cv2.imshow("Original Webcam Feed", frame)
        cv2.imshow("Color Tracking", output)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()