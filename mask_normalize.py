import cv2
import os
import threading
import numpy as np
import pandas as pd

class mask_normalizer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dataUsage = ["gtFine"]
        datasetType = ["train", "val", "test"]
        for duIdx in range(len(dataUsage)):
            for datasetTypeIdx in range(len(datasetType)):
                img_dir = os.path.join(os.getcwd(), "cityscapes", dataUsage[duIdx], datasetType[datasetTypeIdx], "tooth")
                self.imageLoader(img_dir)

    def imageLoader(self, img_dir):
        imgList = os.listdir(img_dir)
        for imgIdx in range(len(imgList)):
            filename = os.path.join(img_dir, imgList[imgIdx])
            print("processing filename : {}".format(filename))
            img = cv2.imread(filename)

            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    b, g, r = img[i,j]
                    if b >= 200 or g >= 200 or r >= 200:
                        # Change the pixel value to a desired value
                        img[i,j] = [255, 255, 255]

                    if b < 200 or g < 200 or r < 200:
                        img[i,j] = [0, 0, 0]
            # cv2.imshow(,img)
            final_filename, _ = os.path.splitext(filename)
            saveFilename = final_filename + ".png"
            cv2.imwrite(saveFilename, img)
            os.remove(filename)
            # print(img[xIdx][yIdx])

class check_normalizedData(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dataUsage = ["gtFine"]
        datasetType = ["train", "val", "test"]
        for duIdx in range(len(dataUsage)):
            for datasetTypeIdx in range(len(datasetType)):
                img_dir = os.path.join(os.getcwd(), "cityscapes", dataUsage[duIdx], datasetType[datasetTypeIdx], "tooth")
                self.imageLoader(img_dir)

    def imageLoader(self, img_dir):
        imgList = os.listdir(img_dir)
        for imgIdx in range(len(imgList)):
            filename = os.path.join(img_dir, imgList[imgIdx])
            img = cv2.imread(filename)
            x = img.shape[0]
            y = img.shape[1]

            cleaness = 0

            for xIdx in range(x):
                for yIdx in range(y):
                    print(img[xIdx][yIdx])
                    if np.any(img[xIdx][yIdx]!= 255) and np.any(img[xIdx][yIdx]!=0):
                        cleaness+=1
            
            if cleaness !=0:
                print("im not clean {}".format(imgList[imgIdx]))

if __name__=="__main__":
    app = mask_normalizer()
    # app = check_normalizedData()