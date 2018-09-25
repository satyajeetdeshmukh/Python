# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:22:00 2018

@author: satya
"""

import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'D:\\Studies\\PYTHON\\opencv\\Output.avi'
    cap = cv2.VideoCapture(filename)
    
    
    while (cap.isOpened()):
    
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()    
    cap.release()

if __name__ == "__main__":
    main()