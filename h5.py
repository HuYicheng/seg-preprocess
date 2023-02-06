import h5py


File_Path='/home/yicheng/Downloads/Swin-Unet/data/Synapse/test_vol_h5/case0001.npy.h5'

f = h5py.File(File_Path,'r')   #打开h5文件
print(f.keys())                            #可以查看所有的主键
image = f['image'][:]                    #取出主键为data的所有的键值
label = f['label'][:]
print(image)
print(image.shape)
print(label)
print(label.shape)
f.close()

