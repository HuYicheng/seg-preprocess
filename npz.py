import numpy as np
import cv2

#data = np.load('/home/yicheng/Downloads/Swin-Unet/data/Synapse/train_npz/case0005_slice000.npz')
data = np.load('/home/yicheng/Downloads/miccai/sensei/train/0.npz')
print(data.files)
image=data['image']
label=data['label']

print(image.shape)
print(label.shape)

cv2.imshow('image',image)
cv2.imshow('label',label)
cv2.waitKey(0)