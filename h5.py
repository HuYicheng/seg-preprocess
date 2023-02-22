import h5py
import cv2

#File_Path='/home/yicheng/Downloads/Swin-Unet/data/Synapse/test_vol_h5/case0001.npy.h5'
File_Path='/home/yicheng/Downloads/miccai/sensei/test_laser/4.npy.h5'

f = h5py.File(File_Path,'r')   #打开h5文件
print(f.keys())                            #可以查看所有的主键
image = f['image'][:]                    #取出主键为data的所有的键值
label = f['label'][:]
print(image.shape)
#cv2.imshow('label',label[0,:,:])
print(sum(sum(label[0,:,:])))
#cv2.imshow('image',image[0,:,:])
cv2.waitKey(0)
print(label.shape)
f.close()

