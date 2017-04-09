import numpy as np
import operator
import YML

def finalresult(seg_swin,num_frame,resultdir,videoname):

    # update seg_swin: choose segment that are not background
    new_seg_swin = []
    for row in seg_swin:
        if int(row[3]) != 0 and float(row[-1])>0.7:
            new_seg_swin.append(row)
    seg_swin = new_seg_swin
    #writelist(r'.\test\1-1',seg_swin)
    # NMS
    overlap_nms = 0
    pick_nms = []
    for cls in range(51):
        zipped = [(idx, [seg_swin[idx][1], seg_swin[idx][2], seg_swin[idx][-1]]) for idx, row in enumerate(seg_swin) if
                  row[3] - 1 == cls]
        if len(zipped) > 0:
            [inputpick, valuepick] = zip(*zipped)
        else:
            continue
        pick_nms.extend([inputpick[idx] for idx in nms_temporal(valuepick, overlap_nms)])
    new_seg_swin = []
    new_seg_swin = [seg_swin[idx] for idx in pick_nms]
    seg_swin = new_seg_swin
    #writelist(r'.\test\2-1', seg_swin)
    # # --------------------- # #
    # # --- output result --- # #
    # # --------------------- # #

    # final localization prediction
    seg_swin = sorted(seg_swin, key=lambda x: x[-1])  # sort and get index
    # f = file(r'F:\icme\result2.txt', 'a+')
    # for data in seg_swin:
    #     k = ' '.join([str(j) for j in data])
    #     f.write(k + "\n")
    # f.close()
    res = [[0] * num_frame for _ in range(52)]  # 20 classes, n frames
    for row in seg_swin:
        for item in range(int(row[1] - 1), int(row[2] + 1)):
            res[int(row[3])][item] = row[4]
    res=np.array(res)
    writelist(r'3-1', res)
    result=[ np.argmax(res[:,_]) for _ in range(num_frame)]
    label=tolabel(result)

    f = file(resultdir+videoname+'.txt', 'w+')
    for data in label:
        k = ' '.join([str(j) for j in data])
        f.write(k + "\n")
    f.close()


def nms_temporal(boxes, overlap):
    pick = []

    if len(boxes)==0:
        return pick
    s = [b[-1] for b in boxes]
    I = [i[0] for i in sorted(enumerate(s), key=lambda x: x[1])]  # sort and get index
    pick.append(I[-1])
    '''
    x1 = [b[0] for b in boxes]
    x2 = [b[1] for b in boxes]
    s = [b[-1] for b in boxes]
    union = map(operator.sub, x2, x1) # union = x2-x1
    I = [i[0] for i in sorted(enumerate(s), key=lambda x:x[1])] # sort and get index

    while len(I)>0:
        i = I[-1]
        pick.append(i)

        xx1 = [max(x1[i],x1[j]) for j in I[:-1]]
        xx2 = [min(x2[i],x2[j]) for j in I[:-1]]
        inter = [max(0.0, k2-k1) for k1, k2 in zip(xx1, xx2)]
        o = [inter[u]/(union[i] + union[I[u]] - inter[u]) for u in range(len(I)-1)]
        I_new = []
        for j in range(len(o)):
            if o[j] <=overlap:
                I_new.append(I[j])
        I = I_new
        '''
    return pick

def tolabel(result):
    label=[]
    temp=result[0]
    index=2
    start=1
    for item in result[1:]:
        if item!=temp:
            if temp!=0:
                label.append([temp,start,index-1])
            temp=item
            start=index
            index+=1
        else:
            index+=1

    #3/31 add
    label2=[]
    i=0
    while i<len(label):
        j=i+1
        while j<len(label) and label[j][0]==label[i][0] :
            j+=1
        if(j==i+1):
            label2.append(label[i])
        else:
            label2.append([label[i][0],label[i][1],label[j-1][-1]])

        i=j


    return label2


def writelist(filename,list):
    f = file(filename + '.txt', 'w+')
    for data in list:
        k = ' '.join([str(j) for j in data])
        f.write(k + "\n")
    f.close()

def readlist(filename):
    file = open(filename)
    data=[]
    line = file.readline()
    while line:
        data.append(YML.str2float(line.split()))
        line=file.readline()
    return data

