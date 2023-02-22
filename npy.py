import numpy as np
from PIL import Image
import cv2

img2 = np.load('/home/yicheng/Downloads/miccai/data_new/data/train/right/img_off_line_annotation/23.npy')
cv2.imshow('a',img2*255)
cv2.waitKey(0)

# img2_crop=img2[:,152:1072]
# print(img2_crop.shape)
# img2_resize=cv2.resize(img2_crop,[512,512])
# # print(img2_resize.shape)
# # print(img2_resize)
# print(sum(img2_resize))
# img2_bin = np.where(img2_resize>0.5,1,0)
# print(sum(img2_bin))
# print(img2_bin)
print(sum(sum(img2)))