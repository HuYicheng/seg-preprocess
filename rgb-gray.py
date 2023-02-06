import cv2
import h5py
import numpy as np
INPUT_PATH='/home/yicheng/Downloads/miccai/sensei/lasersegmapcrop/0.png'
OUPUT_PATH='/home/yicheng/Downloads/miccai/sensei/laserseggmapgraycrop/0.png'

img = cv2.imread(INPUT_PATH, cv2.IMREAD_UNCHANGED)
#print(img.shape)
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#print(img_gray.shape)
img_resize = cv2.resize(img_gray,[512,512])
#print(img_resize.shape)
#cv2.imwrite(OUPUT_PATH, img_resize)

img2=cv2.imread('/home/yicheng/Downloads/miccai/sensei/lasersegmapcrop/0.jpg')
#print(img2.shape)
img2_gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
#print(img2_gray.shape)
img2_resize=cv2.resize(img2_gray,[512,512])
#print(img2_resize.shape)
cv2.imshow('img2_resize',img2_resize)
cv2.imshow('img1_resize',img_resize)
# print(img_resize.shape)
# print(img2_resize.shape)
# cv2.waitKey(0)

h5_path='/home/yicheng/Downloads/miccai/sensei/laserseggmapgraycrop/a.npy.h5'

with h5py.File(h5_path, 'w') as hf:
    hf.create_dataset('image',  data=img_resize[np.newaxis,:])
    hf.create_dataset('label',data=img2_resize[np.newaxis,:])

f = h5py.File(h5_path,'r')
print(f.keys())
image = f['image'][:]
label = f['label'][:]
print(image)
print(image.shape)
print(label)
print(label.shape)
f.close()






