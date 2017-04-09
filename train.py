import os
import numpy as np
from keras.utils import np_utils
from lstm import model

path='E:/BaiduYunDownload/STRUCT_ICMEW/'
dataPath=path+'divide_frame/'
traindataPath=dataPath+'train/'
testdataPath=dataPath+'test/'

timestep=10

trainFileList=os.listdir(traindataPath)
testFileList=os.listdir(testdataPath)

train_labels=[]
train_datas=[]
test_labels=[]
test_datas=[]

#count=0
def dataGenerate():
    for item in trainFileList:
        train_data=[]
        train_label=(item.split('.')[0].split('-')[2])
        train_labels.append(train_label)
        f=open(traindataPath+item)
        line=f.readline()
        while line:
            train_data.append(line)
            line=f.readline()
        for i in range(len(train_data)-timestep):
            data_train=np.array([train_data[j]for j in range(i,i+timestep)])
            label_train=np_utils.to_categorical(train_label,51)
            yield (data_train,label_train)
            count+=1
        train_data=[]
        train_datas.append(train_data)
    #return count
    
def dataGenerate2(count):
    for item in testFileList:
        test_data=[]
        test_label=(item.split('.')[0].split('-')[2])
        test_labels.append(test_label)
        f=open(testdataPath+item)
        line=f.readline()
        while line:
            test_data.append(line)
            line=f.readline()
        for i in range(len(test_data)-timestep):
            data_test=np.array([test_data[j]for j in range(i,i+timestep)])
            label_test=np_utils.to_categorical(test_label,51)
            yield (data_test,label_test)
            count+=1
        test_data=[]
        test_datas.append(test_data)
    #return count
    
model.fit_generator(dataGenerate(),samples_per_epoch=1987819, nb_epoch=10,verbose=1,
                    validation_data=dataGenerate2(),
                    nb_val_samples=259607)

model.save_weights('my_weights/pku_train_lstm'+str(0)+'.h5')

print 'the end!'


