import os
import numpy as np
from keras.utils import np_utils
#from lstm import model

def getdata():
    path='E:/BaiduYunDownload/STRUCT_ICMEW/'
    dataPath=path+'divide_frame/'
    traindataPath=dataPath+'train/'
    testdataPath=dataPath+'test/'
    
    trainFileList=os.listdir(traindataPath)
    testFileList=os.listdir(testdataPath)
    
    timestep=10
    
    train_labels=[]
    train_datas=[]
    test_labels=[]
    test_datas=[]
    data_banch=np.empty((1,timestep,150),dtype="float32")
    label_batch=[]
    
    for item in trainFileList:
        train_data=[]
        train_label=(item.split('.')[0].split('-')[2])
        train_labels.append(train_label)  
        #print train_labels
        f=open(traindataPath+item)
        line=f.readline()
        while line:           
            train_data.append(line.split(' '))
            line=f.readline()  
        for i in range(len(train_data)-timestep):
            data_train=np.array([train_data[j]for j in range(i,i+timestep)])
            label_train=np_utils.to_categorical([train_label],51)
            label_batch.append(label_train) 
            data_train=np.expand_dims(data_train,axis=0)
            data_banch=np.concatenate((data_banch,data_train),axis=0)        
        #train_datas.append(data_train)
        #print np.array(data_banch).shape,np.array(label_batch).shape
    return np.array(data_banch),np.array(label_batch)
 