import cv2
import numpy as np
import os

def func(impath):
    frame = cv2.imread(impath)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_frame, (5, 5), 2)

    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    ret, res = cv2.threshold(thresh, 70, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return res



if not os.path.exists("dataset"):
    os.makedirs("dataset")
if not os.path.exists("dataset/train"):
    os.makedirs("dataset/train")
if not os.path.exists("dataset/test"):
    os.makedirs("dataset/test")

path = "train"
path1 = "dataset"
a = ['label']

for i in range(64 * 64):
    a.append("pixel" + str(i))


label = 0
var = 0
c1 = 0
c2 = 0

for (dirpath, dirnames, filenames) in os.walk("C:/Users/Asus/Desktop/Sign_lang/asl_dataset"):
    for dirname in dirnames:
        print(dirname)
        for (direcpath, direcnames, files) in os.walk("C:/Users/Asus/Desktop/Sign_lang/asl_dataset/" + dirname):
            if not os.path.exists(path1 + "/train/" + dirname):
                os.makedirs(path1 + "/train/" + dirname)
            if not os.path.exists(path1 + "/test/" + dirname):
                os.makedirs(path1 + "/test/" + dirname)

            num=0.75*len(files)

            i = 0
            for file in files:
                var += 1
                actual_path = "C:/Users/Asus/Desktop/Sign_lang/asl_dataset/" + dirname + "/" + file
                actual_path_train = path1 + "/" + "train/" + dirname + "/" + file
                actual_path_test = path1 + "/" + "test/" + dirname + "/" + file
                img = cv2.imread(actual_path)
                bw_image = func(actual_path)
                if i < num:
                    c1 += 1
                    cv2.imwrite(actual_path_train, bw_image)
                else:
                    c2 += 1
                    cv2.imwrite(actual_path_test, bw_image)

                i = i + 1

        label = label + 1
print(var)
print(c1)
print(c2)