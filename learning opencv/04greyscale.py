# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:45:22 2018

@author: satya
"""

import cv2 #imports opencv

def main():
    print("starting...")
    imgpath = "D:\\Studies\\PYTHON\\opencv\\database\\lena_color_256.tif"
    img = cv2.imread(imgpath, 0)
    
    """
    img = cv2.imread(imgpath, 1) #load by saving all color info in the image [default]
    img = cv2.imread(imgpath, 0) #read in greyscale mode
    img = cv2.imread(imgpath, -1) #reads image as it is and also saves alpha transperanc
    
    """
    
    print("import success")
    
    outpath = "D:\\Studies\\PYTHON\\opencv\\output\\lena_color_256.jpg"
    cv2.imwrite(outpath, img)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    

if __name__ == "__main__":
    main()