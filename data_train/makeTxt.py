#! /usr/bin/python3
import os
import random
 
 
trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = '/home/lsn/yolov5-6.0/data_/Annotations'
txtsavepath = '/home/lsn/yolov5-6.0/data_/ImageSets'
total_xml = os.listdir(xmlfilepath)
 
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
 
ftrainval = open('/home/lsn/yolov5-6.0/data_/ImageSets/trainval.txt', 'w')
ftest = open('/home/lsn/yolov5-6.0/data_/ImageSets/test.txt', 'w')
ftrain = open('/home/lsn/yolov5-6.0/data_/ImageSets/train.txt', 'w')
fval = open('/home/lsn/yolov5-6.0/data_/ImageSets/val.txt', 'w')
 
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
