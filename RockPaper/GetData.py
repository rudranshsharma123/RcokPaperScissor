import os
import sys
from cv2 import cv2
import numpy as np
try:
    label_names = sys.argv[1]
    num = int(sys.argv[2])
except FileExistsError:
    print("args not provided")
    exit(-1)

dir_name = "train_images"
path = os.path.join(dir_name, label_names)

try:
    os.mkdir(os.getcwd()+"\\"+path)
except FileExistsError:
    print("The dir exists adding more images into the dir")
    pass

cam = 
