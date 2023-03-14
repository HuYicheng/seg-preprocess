# test_in = '/home/yicheng/Downloads/miccai/sensei/split_diffusion/test.txt'
# train_in = '/home/yicheng/Downloads/miccai/sensei/split_diffusion/train.txt'
#
# test_out = '/home/yicheng/Downloads/miccai/sensei/lists/test.txt'
# train_out = '/home/yicheng/Downloads/miccai/sensei/lists/train.txt'
#
# test_in=open(test_in, mode="r")
# test_out=open(test_out, mode="w")
# line = test_in.readline()
# while line:
#     case=line[15:-5]
#     print(case)
#     test_out.write(case+'\n')
#     line = test_in.readline()
# test_in.close()
# test_out.close()
#
# train_in=open(train_in, mode="r")
# train_out=open(train_out, mode="w")
# line = train_in.readline()
# while line:
#     case=line[15:-5]
#     print(case)
#     train_out.write(case+'\n')
#     line = train_in.readline()
# train_in.close()
# train_out.close()

import os
path_train='/home/yicheng/Downloads/miccai/Prossed-full-data/train/left/rgb'
path_val='/home/yicheng/Downloads/miccai/Prossed-full-data/val/left/rgb'
path_test='/home/yicheng/Downloads/miccai/Prossed-full-data/test/left/rgb'

list_train='/home/yicheng/Downloads/miccai/Prossed-full-data/list/train.txt'
list_val='/home/yicheng/Downloads/miccai/Prossed-full-data/list/val.txt'
list_test='/home/yicheng/Downloads/miccai/Prossed-full-data/list/test.txt'


train=os.listdir(path_train)
train_out=open(list_train, mode="w")
for case_train in train:
    print(case_train[:-4])
    train_out.write(case_train[:-4] + '\n')
train_out.close()

print('list of train has been generated successfully')

val=os.listdir(path_val)
val_out=open(list_val, mode="w")
for case_val in val:
    print(case_val[:-4])
    val_out.write(case_val[:-4] + '\n')
val_out.close()

print('list of val has been generated successfully')



test=os.listdir(path_test)
test_out=open(list_test, mode="w")
for case_test in test:
    print(case_test[:-4])
    test_out.write(case_test[:-4] + '\n')
test_out.close()

print('list of test has been generated successfully')