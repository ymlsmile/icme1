import os
import numpy as np
#from keras.utils import np_utils
#from lstm2 import model

def getdata(traindataPath,timestep):
    #path='E:/BaiduYunDownload/STRUCT_ICMEW/'
    print 'start loaddata...'
    joint=[]
    for i in range(147):
        joint.extend([-1])

    #dataPath='../../dataset/train_test/'#divide_frame/'#path+'divide_frame/'
    #traindataPath=dataPath+'train/'
    #testdataPath=dataPath+'test/'

    trainFileList=os.listdir(traindataPath)
    #testFileList=os.listdir(testdataPath)

    #timestep=32
    count=0
    train_labels=[]
    train_datas=[]
    test_labels=[]
    test_datas=[]
    data_banch=[]#np.empty((1,timestep,150),dtype="float32")
    label_batch=[]
    print 'hhhh'
    for item in trainFileList:
        #print '.',
        count+=1
        if count%1000==0:
            print '.',
        train_data=[]
        #print item
        train_label=int(item.split('.')[0].split('-')[2])-1
        train_labels.append(train_label)
        #print train_labels
        f=open(traindataPath+item)
        line=f.readline()
        while line:
            #train_label=(item.split('.')[0].split('-')[2])
            #train_labels.append(train_label)
            dataline=line.split(' ')
            train_data.append([float(dataline[j])for j in range(150)])
            line=f.readline()
        #print len(train_data)
        if len(train_data)<timestep:
            dif=timestep-len(train_data)
            for i in range(dif):
                #train_data.append(train_data[-1])
                train_data.append(joint)
        train_data=train_data[:timestep]
        #print np.array(train_data).shape
        #label_train=np_utils.to_categorical([train_label],51)
        data_banch.append(train_data)
        #print np.array(data_banch).shape
        label_batch.append(train_label)
        print np.array(label_batch).shape
        print np.array(data_banch).shape
        '''for i in range(0,len(train_data)-timestep,5):
            data_train=np.array([train_data[j]for j in range(i,i+timestep)])
            label_train=np_utils.to_categorical([train_label],51)
            #print np.array(label_train).shape
            label_batch.extend(label_train)
            #print label_batch
            #data_train=np.expand_dims(data_train,axis=0)
            data_banch.append(data_train)#np.concatenate((data_banch,data_train),axis=0)
        '''
        #train_datas.append(data_train)
        #print np.array(data_banch).shape,np.array(label_batch).shape
    print 'loaddata end ...'
    return np.array(data_banch),np.array(label_batch)


def getdatayml(traindataPath,timestep=200,num_actions=51):
    dataFileList = os.listdir(traindataPath)
    #num_data=0
    data_banch = []
    label_batch = []
    for dataFile in dataFileList:
        action_id=int(dataFile.split('-')[2])-1
        label_batch.append(action_id)
        f = open(traindataPath + dataFile)
        line = f.readline()
        step=0
        train_data=[]
        while line:
            if(step>=timestep-1):
                break
            step+=1
            dataline = line.split(' ')
            train_data.append([float(dataline[j]) for j in range(3, 150)])
            #train_data.append([float(dataline[j]) for j in range(3, 150)])
            line = f.readline()

        #num_data+=1
    label_batch=np_utils.to_categorical(label_batch,num_actions)







getdata("F:/icme/data/divide_frame/test/",200)
