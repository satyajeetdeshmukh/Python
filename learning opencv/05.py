# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:45:22 2018

@author: satya
"""

import cv2 #imports opencv

def main():
    print("starting...")
    imgpath = "D:\\Studies\\PYTHON\\opencv\\database\\lena_color_256.tif"
    img1 = cv2.imread(imgpath, 0)
    
#    print(img1) #tuple represents BGR
    print(type(img1))
    print(img1.dtype)
    
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    
#    cv2.imshow('Lena', img1)
#    cv2.waitKey(0)
#    cv2.destroyWindow('Lena')
    
    

if __name__ == "__main__":
    main()