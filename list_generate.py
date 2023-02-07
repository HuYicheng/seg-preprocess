test_in = '/home/yicheng/Downloads/miccai/sensei/split_diffusion/test.txt'
train_in = '/home/yicheng/Downloads/miccai/sensei/split_diffusion/train.txt'

test_out = '/home/yicheng/Downloads/miccai/sensei/lists/test.txt'
train_out = '/home/yicheng/Downloads/miccai/sensei/lists/train.txt'

test_in=open(test_in, mode="r")
test_out=open(test_out, mode="w")
line = test_in.readline()
while line:
    case=line[15:-5]
    print(case)
    test_out.write(case+'\n')
    line = test_in.readline()
test_in.close()
test_out.close()

train_in=open(train_in, mode="r")
train_out=open(train_out, mode="w")
line = train_in.readline()
while line:
    case=line[15:-5]
    print(case)
    train_out.write(case+'\n')
    line = train_in.readline()
train_in.close()
train_out.close()