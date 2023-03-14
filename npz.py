import numpy as np
import cv2

# data = np.load('/home/yicheng/Downloads/Swin-Unet/data/Synapse/train_npz/case0005_slice100.npz')
data = np.load('/home/yicheng/Downloads/miccai/Prossed-full-data/train/left/processed_unet_896/0.npz')
print(data.files)
image=data['image']
label=data['label']

print(type(image))
print(type(label[0,0]))


print(image.shape)
print(label.shape)

cv2.imshow('image',image)
#cv2.imshow('label',label)
print(sum(sum(label)))
cv2.waitKey(0)

