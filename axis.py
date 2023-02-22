import cv2
import numpy as np
import os
from random import sample

line_root='/home/yicheng/Downloads/miccai/data_new/data/train/left/img_off_line/'
out_root='/home/yicheng/Downloads/miccai/data_new/data/train/left/img_off_line_annotation/'
files=os.listdir(line_root)
for file in files:
    line_path=line_root + file
    print(file[:-4])

    img=cv2.imread(line_path)
    img_line=np.where((img[:,:,2]>200)&(img[:,:,1]<40)&(img[:,:,0]>30)&(img[:,:,0]<55),np.uint8(1),np.uint8(0))
    np.save(out_root+file[:-4],img_line)
    #cv2.imshow(file,img_line)
    #cv2.waitKey(300)

print(len(files))