import cv2
import numpy as np
import os
from random import sample

image_root='/home/yicheng/Downloads/miccai/data_new/data/train/right/img_off_line/'
axis_root='/home/yicheng/Downloads/miccai/data_new/data/train/right/img_off_line_annotation/'
sample_root='/home/yicheng/Downloads/miccai/data_new/data/train/right/line_annotation_sample/'
files=os.listdir(axis_root)
for file in files:
    axis_path=axis_root + file
    print(file[:-4])

    annotation=np.load(axis_path)
    a=np.where(annotation != 0)
    a=np.array(a)
    a=a.T
    row_rand_array = np.arange(a.shape[0])
    np.random.shuffle(row_rand_array)
    row_rand = a[row_rand_array[0:50]]
    np.savetxt(sample_root+file[:-4]+'.txt', row_rand,fmt='%.00f')

    image_path = image_root + file[:-4] +'.jpg'
    image = cv2.imread(image_path)
    #print(image.shape)
    for i in row_rand:
        #print(i)
        #print(tuple(i))
        image[i[0], i[1], :] = [0, 0, 0]
        # image[i[1],i[0],:]=[0,0,0]
        k = (i[1], i[0])
        cv2.circle(image, k, radius=5, color=[255, 255, 255])
    cv2.imwrite(sample_root + file[:-4] +'.jpg', image)


