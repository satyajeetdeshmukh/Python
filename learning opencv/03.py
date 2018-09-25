import cv2 #imports opencv

def main():
    print("starting...")
    imgpath = "D:\\Studies\\PYTHON\\opencv\\database\\lena_color_256.tif"
    img = cv2.imread(imgpath)
    print("import success")
    #cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    #cv2.destroyAllwindows()
    cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()