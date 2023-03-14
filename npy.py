import numpy as np
from PIL import Image
import cv2

# img2 = np.load('/media/yicheng/App/Download/Ximea-2023-Phantom-laser-rotate/collectedData/laser/camera1/rgb_line_annotation/50.npy')
img2=cv2.imread('/media/yicheng/App/Download/Ximea-2023-Phantom-laser-rotate/collectedData/laser/camera1/rgb_line/50.jpg')
cv2.namedWindow('a',cv2.WINDOW_NORMAL)
cv2.imshow('a',img2)
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

#(77,3064)
#(2209,2481)
#(77-2209)/(3064-2481)=(77-x)/(3064-y)

#for y in 2481 to 3064
#x=round((y-3064)*(77-2209)/(3064-2481)+77)
#list.append([x,y])