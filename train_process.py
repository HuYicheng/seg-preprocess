import cv2
import numpy as np
import os
from torchvision import transforms
from PIL import Image
import torch

# RGB_ROOT ='/home/yicheng/Downloads/miccai/sensei/RGBdata/left/'
# Seg_ROOT='/home/yicheng/Downloads/miccai/sensei/lasersegmap/'
# npz_ROOT='/home/yicheng/Downloads/miccai/sensei/train/'
# list_path='/home/yicheng/Downloads/miccai/sensei/split_diffusion/train.txt'

RGB_ROOT ='/home/yicheng/Downloads/miccai/Prossed-full-data/train/left/rgb/'
Seg_ROOT='/home/yicheng/Downloads/miccai/Prossed-full-data/train/left/segmap/'
npz_ROOT='/home/yicheng/Downloads/miccai/Prossed-full-data/train/left/processed_unet_896/'
list_path='/home/yicheng/Downloads/miccai/Prossed-full-data/list/train.txt'

if not os.path.exists(npz_ROOT):
    os.mkdir(npz_ROOT)

file=open(list_path, mode="r")
line = file.readline()
while line:
    case=line[:-1]
    print (case)
    #print(type(line))

    RGB_INPUT_PATH=RGB_ROOT+case+'.jpg'
    Seg_PATH=Seg_ROOT+case+'.npy'
    npz_PATH=npz_ROOT+case+'.npz'

    #print(RGB_INPUT_PATH)

    # img = cv2.imread(RGB_INPUT_PATH, cv2.IMREAD_UNCHANGED)
    img=Image.open(RGB_INPUT_PATH)
    #print(img.shape)
    transform = transforms.Compose([transforms.ToTensor(), transforms.Grayscale(num_output_channels=1)])
    img_gray=transform(img)
    # img_crop=transforms.functional.crop(img_gray,0,0,896,896)
    img_crop=img_gray[0:896,0:896]
    img_crop=torch.squeeze(img_crop)
    # transform=transforms.Compose([transforms.ToTensor(),transforms.Grayscale(num_output_channels=1),transforms.functional.crop(,0,0,896,896)])
    # img_crop=transform(img)
    # img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # img_gray=img.convert('L')
    #print(img_gray.shape)
    # img_crop=T.functional.crop(img_gray,0,0,896,896)
    # img_crop=img_gray[0:896,0:896]
    # img_norm = (img_crop - np.min(img_crop)) / (np.max(img_crop) - np.min(img_crop))

    #img2=cv2.imread(Seg_PATH,cv2.IMREAD_UNCHANGED)
    img2=np.load(Seg_PATH)
    # img2=Image.open(Seg_PATH)
    #img2_gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
    #print(img2_gray.shape)
    # img2_crop=img2[12:908,164:1060]
    img2_crop=np.float32(img2[0:896,0:896])
    #print(img2_crop.shape)
    #img2_resize=cv2.resize(img2_crop,[512,512])
    #print(img2_resize.shape)
    #img2_bin = np.where(img2_resize>0.5,np.uint8(1),np.uint8(0))
    # cv2.imshow('img2_resize',img2_resize)
    # cv2.imshow('img_resize',img_resize)
    # cv2.imshow('img2_bin',img2_bin)
    #print(img_resize.shape)
    #print(img2_resize.shape)
    #cv2.waitKey(0)
    #
    #
    np.savez(npz_PATH,image=img_crop, label=img2_crop)

    line = file.readline()
file.close()





