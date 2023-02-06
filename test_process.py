import cv2
import h5py
import numpy as np

RGB_ROOT ='/home/yicheng/Downloads/miccai/sensei/RGBdata/left/'
Seg_ROOT='/home/yicheng/Downloads/miccai/sensei/lasersegmap/'
h5_ROOT='/home/yicheng/Downloads/miccai/sensei/test/'
list_path='/home/yicheng/Downloads/miccai/sensei/split_diffusion/test.txt'

file=open(list_path, mode="r")
line = file.readline()
while line:
    case=line[15:-5]
    print (case)
    #print(type(line))

    RGB_INPUT_PATH=RGB_ROOT+case+'.jpg'
    Seg_PATH=Seg_ROOT+case+'.jpg'
    h5_PATH=h5_ROOT+case+'.npy.h5'

    img = cv2.imread(RGB_INPUT_PATH, cv2.IMREAD_UNCHANGED)
    #print(img.shape)
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #print(img_gray.shape)
    img_crop=img_gray[:,152:1072]
    #print(img_crop.shape)
    img_resize = cv2.resize(img_crop,[512,512])
    #print(img_resize.shape)

    img2=cv2.imread(Seg_PATH,cv2.IMREAD_UNCHANGED)
    #img2_gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
    #print(img2_gray.shape)
    img2_crop=img2[:,152:1072]
    #print(img2_crop.shape)
    img2_resize=cv2.resize(img2_crop,[512,512])
    #print(img2_resize.shape)
    thre,img2_bin = cv2.threshold(img2_resize,30,1,cv2.THRESH_BINARY)
    # cv2.imshow('img2_resize',img2_resize)
    # cv2.imshow('img_resize',img_resize)
    # cv2.imshow('img2_bin',img2_bin)
    #print(img_resize.shape)
    #print(img2_resize.shape)
    #cv2.waitKey(0)
    #
    #
    with h5py.File(h5_PATH, 'w') as hf:
        hf.create_dataset('image',  data=img_resize[np.newaxis,:])
        hf.create_dataset('label',data=img2_bin[np.newaxis,:])

    #f = h5py.File(h5_PATH,'r')
    #print(f.keys())
    # image = f['image'][:]
    # label = f['label'][:]
    #print(image)
    #print(image.shape)
    #print(label)
    #print(label.shape)
    #f.close()


    line = file.readline()
file.close()





