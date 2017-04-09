# -*- coding: utf-8 -*-
import os
import numpy as np
import random
import math
#from keras.utils import np_utils
#from keras import backend as K

#from CNNetmodel import model

path='D:/g470/icme/data/'
dataPath=path+'PKU_Skeleton_Renew/'
labelPath=path+'Train_Label_PKU_final/'

clusterlen=[39,63,73,82,92,102,112,123,
            134,  144,  154,  178,  188,
            205,  218,  228,  238,  254,
            264,  277,  298,  315,  325,
            343,  353,  367,  397,  413,
            424,  443,  454,  475,  489]
cross_subject=open(path+'cross-subject.txt')

tbool=1
trainfile=[]
testfile=[]
line=cross_subject.readline()
while line:
    if line!='Validataion videos: \n' and tbool==1 and line!='Training videos: \n':
        trainfile=line.split(', ') 
    if line=='Validataion videos: \n':
        tbool=0
    if tbool==0:
        testfile=line.split(', ')
    line=cross_subject.readline()
#print np.array(trainfile), np.array(testfile)     

skeletonfiles=os.listdir(dataPath)


def loaddata2(datapath,labelpath,tr,item):
    print item
    traindata=[]
    testdata=[]
    label=[]
    actionfile=open(datapath)
    labelfile=open(labelpath)
    count=1          #起始帧为第0帧
    line_label=labelfile.readline()
    while line_label:
        label.append(line_label.split(','))
        #print '.',
        line_label=labelfile.readline()
        
    line=actionfile.readline()
    i=0
    #print '/n start write divide frame'
    while line:
        #print '.',
        if i>=len(label):
            break
        if count<int(label[i][1]):
            if tr == 1:
                f = file(path + 'background/train/' + item + '-0-' + str(i) + '.txt', 'a+')
            else:
                f = file(path + 'background/test/' + item + '-0-' + str(i) + '.txt', 'a+')
            f.write(line)
            f.close()

        #if count<int(label[i][2]):

        if count==int(label[i][2]):
            i+=1
        count+=1
        line = actionfile.readline();



        # if count>=int(label[i][1]) and count<=int(label[i][2]):
        #     bo=1
        #     if tr==1:
        #         #f=file(path+'divide_frame/train/'+item+'-'+label[i][0]+'.txt','a+')
        #         traindata.append(line)
        #         #f.write(line)
        #         #f.close()
        #     else:
        #         f=file(path+'divide_frame/test/'+item+'-'+label[i][0]+'.txt','a+')
        #         testdata.append(line)
        #         #f.write(line)
        #         f.close()
        # else:
        #     bo=0
        # if (len(traindata) or len(testdata)) and bo==0:
        #     i+=1
        #     traindata=[]
        #     testdata=[]
        # count+=1
        # line=actionfile.readline()


def decidelocation(dl,fl,iou):
    return int(math.ceil((fl+dl)*iou/(iou+1)))


def dividedata(datapath,labelpath,tr,item):
    print item
    traindata=[]
    testdata=[]
    label=[]
    actiondata=[]
    actionfile=open(datapath)
    labelfile=open(labelpath)
    count=1          #起始帧为第0帧
    line_label=labelfile.readline()
    while line_label:
        label.append(line_label.split(','))
        #print '.',
        line_label=labelfile.readline()
    #line=actionfile.readline()
    actionline=actionfile.readline()
    while actionline:
        actiondata.append(actionline.split())
        actionline=actionfile.readline()
    for index in range(len(label)):

        classindex=label[index][0]
        startindex=int(label[index][1])
        endindex=int(label[index][2])
        framelength=endindex-startindex
        for i in range(2):
            left=math.ceil(0.7*framelength)
            right=math.floor(1.4*framelength)
            if(left>=right):
                break
            dividelength=random.randint(left,right)
            IOU=random.uniform(0.7,1.0)
            overlap=decidelocation(dividelength,framelength,IOU)
            divideend=startindex+overlap-1
            dividestart=divideend-dividelength+1
            dividestart2=endindex-overlap+1
            divideend2=dividestart2+dividelength-1
            didata1=actiondata[dividestart-1:divideend]
            if tr == 1:
                f=file(path+'divide_frame/train/'+item+'-'+classindex+'-'+str(i*2)+'-%.2f.txt'%(IOU),'a+')
            else:
                f=file(path+'divide_frame/test/'+item+'-'+classindex+'-'+str(i*2)+'-%.2f.txt'%(IOU),'a+')
            for data in didata1:
                k = ' '.join([str(j) for j in data])
                f.write(k + "\n")
            f.close()
            didata2 = actiondata[dividestart2 - 1:divideend2]
            if tr == 1:
                f = file(
                    path + 'divide_frame/train/' + item + '-' + classindex + '-' + str(i * 2+1) + '-%.2f.txt' % (IOU),
                    'a+')
            else:
                f = file(path + 'divide_frame/test/' + item + '-' + classindex + '-' + str(i * 2+1) + '-%.2f.txt' % (IOU),
                         'a+')
            for data in didata2:
                k = ' '.join([str(j) for j in data])
                f.write(k + "\n")
            f.close()

def dividedata0(datapath,labelpath,tr,item):
    print item
    traindata=[]
    testdata=[]
    label=[]
    actiondata=[]
    actionfile=open(datapath)
    labelfile=open(labelpath)
    count=1          #起始帧为第0帧
    line_label=labelfile.readline()
    while line_label:
        label.append(line_label.split(','))
        #print '.',
        line_label=labelfile.readline()
    #line=actionfile.readline()
    actionline=actionfile.readline()
    while actionline:
        actiondata.append(actionline.split())
        actionline=actionfile.readline()
    videolength=len(actiondata)
    for index in range(len(label)):

        classindex=label[index][0]
        startindex=int(label[index][1])
        endindex=int(label[index][2])
        framelength=endindex-startindex
        left = math.ceil(0.7 * framelength)
        right = math.floor(1.4 * framelength)
        if (left >= right):
            break
        for i in range(2):

            dividelength=random.randint(left,right)
            IOU=random.uniform(0,0.3)
            overlap=decidelocation(dividelength,framelength,IOU)
            divideend=max(startindex+overlap-1,1)
            dividestart=max(divideend-dividelength+1,1)
            dividestart2=min(endindex-overlap+1,videolength)
            divideend2=min(dividestart2+dividelength-1,videolength)
            didata1=actiondata[dividestart-1:divideend]
            if tr == 1:
                f=file(path+'divide_frame0/train/'+item+'-0-'+str(index)+'-'+str(i*2)+'-%.2f.txt'%(IOU),'a+')
            else:
                f=file(path+'divide_frame0/test/'+item+'-0-'+str(index)+'-'+str(i*2)+'-%.2f.txt'%(IOU),'a+')
            for data in didata1:
                k = ' '.join([str(j) for j in data])
                f.write(k + "\n")
            f.close()
            didata2 = actiondata[dividestart2 - 1:divideend2]
            if tr == 1:
                f = file(
                    path + 'divide_frame0/train/' + item + '-0-'+str(index)+'-' + str(i * 2+1) + '-%.2f.txt' % (IOU),
                    'a+')
            else:
                f = file(path + 'divide_frame0/test/' + item + '-0-'+str(index)+'-' + str(i * 2+1) + '-%.2f.txt' % (IOU),
                         'a+')
            for data in didata2:
                k = ' '.join([str(j) for j in data])
                f.write(k + "\n")
            f.close()

def dividebackground(dir,tr):
    count1=0;count2=0;count3=0
    files=os.listdir(dir)
    for file in files:
        filename=os.path.splitext(file)[0];
        f=open(os.path.join(dir,file))
        lines = len(f.readlines())
        if lines<200:
            count1+=1
        else:
            if lines<400:
                count2+=1
            else:
                count3+=1
    print count1, count2, count3



        # item='0043-L'
# dividedata(dataPath + item + '.txt', labelPath + item + '.txt', 1, item)

# for item in skeletonfiles:
#     item=item.split('.')[0]
#     if item in trainfile:
#         loaddata2(dataPath+item+'.txt',labelPath+item+'.txt',1,item)
#         #dividedata0(dataPath + item + '.txt', labelPath + item + '.txt', 1, item)
#     if item in testfile:
#         loaddata2(dataPath+item+'.txt',labelPath+item+'.txt',0,item)
#         #dividedata0(dataPath + item + '.txt', labelPath + item + '.txt', 0, item)
#dividebackground("F:/icme/data/background/train",1)
print 'end'
    