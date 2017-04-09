import finalresult
import os
import numpy as np
dataPath = r"D:\g470\icme\data\PKU_Skeleton_Renew/"
midresultpath=r"D:\g470\icme\data\net2result/"
resultpath=r"D:\g470\icme\data\labels/"
midresult=os.listdir(midresultpath)
for mid in midresult:
    #print os.path.splitext(mid)[1]
    if os.path.splitext(mid)[1]=='.npy':
        item=os.path.splitext(mid)[0]
        f=open(dataPath+item+'.txt')
        framelen=len(f.readlines())
        seg_swin = np.load(midresultpath+mid)
        finalresult.finalresult(seg_swin, framelen,resultpath,item)


