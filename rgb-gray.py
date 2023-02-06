import cv2
INPUT_PATH='/home/yicheng/Downloads/miccai/sensei/lasersegmapcrop/0.png'
OUPUT_PATH='/home/yicheng/Downloads/miccai/sensei/laserseggmapgraycrop/0.png'

img = cv2.imread(INPUT_PATH, cv2.IMREAD_UNCHANGED)
shape = img.shape
print(shape)
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img_gray.shape)
img_resize = cv2.resize(img_gray,[512,512])
print(img_resize.shape)
cv2.imwrite(OUPUT_PATH, img_resize)

img1=cv2.imread(OUPUT_PATH, cv2.IMREAD_UNCHANGED)
print(img1.shape)