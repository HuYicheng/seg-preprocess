import cv2
import numpy as np

laser_ROOT ='/home/yicheng/Downloads/miccai/sensei/laserdata/left/'
Seg_ROOT='/home/yicheng/Downloads/miccai/sensei/lasersegmap/'
npz_ROOT='/home/yicheng/Downloads/miccai/sensei/train_laser/'
list_path='/home/yicheng/Downloads/miccai/sensei/split_diffusion/train.txt'

file=open(list_path, mode="r")
line = file.readline()
while line:
    case=line[15:-5]
    print (case)
    #print(type(line))

    RGB_INPUT_PATH=laser_ROOT+case+'.jpg'
    Seg_PATH=Seg_ROOT+case+'.jpg'
    npz_PATH=npz_ROOT+case+'.npz'

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
    np.savez(npz_PATH,image=img_resize, label=img2_bin)

    line = file.readline()
file.close()





