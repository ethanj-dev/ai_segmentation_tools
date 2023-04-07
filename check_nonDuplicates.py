import os
from pathlib import Path
import threading
import shutil

## Needs fixing

class nonDuplicates(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.checkDatasetTree()

    def checkDatasetTree(self):
        currentDir = str(os.getcwd())
        img_dir = os.path.join(currentDir, "cityscapes", "leftImg8bit")
        label_dir = os.path.join(currentDir, "cityscapes", "gtFine")

        data_folder = ["train", "test", "val"]

        for dataFolderIdx in range(len(data_folder)):
            img_folder = os.path.join(img_dir, data_folder[dataFolderIdx], "tooth")
            label_folder = os.path.join(label_dir, data_folder[dataFolderIdx],"tooth")
            img_list = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]
            imgSize = len(img_list)

            print(img_folder)

            label_list = [f for f in os.listdir(label_folder) if os.path.isfile(os.path.join(label_folder, f))]
            labelSize = len(label_list)

            if imgSize > labelSize:
                self.compareFiles(img_list, label_list, img_folder)
            elif imgSize <labelSize:
                self.compareFiles(label_list, img_list, label_folder)
            else:
                self.compareFiles(img_list, label_list, img_folder)
                self.compareFiles(label_list, img_list, label_folder)

            print("Finished comparing Data : {}".format(data_folder[dataFolderIdx]))

            

    def compareFiles(self, highestQA_list, lowestQA_list, dir):
        

        for imgIdx in range(len(highestQA_list)):
            same = 0
            imgName = os.path.splitext(highestQA_list[imgIdx])[0]

            for idx in range(len(lowestQA_list)):
                compImgName = os.path.splitext(lowestQA_list[idx])[0]


                if imgName == compImgName:
                    same+=1
            if same == 0:
                filename = os.path.join(dir, highestQA_list[imgIdx])
                os.remove(filename)
                # print(filename)

if __name__=="__main__":
    app = nonDuplicates()