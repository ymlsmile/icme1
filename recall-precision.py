# -*- coding: utf-8 -*-
import pandas as pd
import os
 
def IOU(start1, end1, start2, end2):
    print 'compute IoU....'
    print start1
    print end1
    print start2
    print end2
    x1 = min(start1,start2)
    y1 = max(end1,end2)
    x2 = max(start1,start2)
    y2 = min(end1,end2)
    if x2 >= y2 : #没有重叠
        IoU = 0
        print IoU
        return IoU
    intersection = y2-x2
    union = y1-x1 
    IoU = intersection/union
    print intersection
    print union
    print IoU
    return IoU
 
print 'start....'
dir = r'D:\g470\icme\data\labels'
for root,dirs,files in os.walk(dir):
    for file in files:
        filename = os.path.join(file)
        label_filename = dir + '/' + filename
        print label_filename
        for line in open(label_filename):
            annotation_filename = r'D:\g470\icme\data\Train_Label_PKU_final/' + filename
            print annotation_filename  
            x = line.find(' ')
            y = line.find(' ',x+1)
            label = line[0:x]
            start = line[x+1:y]
            end = line[y+1:len(line)-1] 
            print 'label = ', label, 'start = ', start, 'end = ', end
            for line2 in open(annotation_filename):    
                m = line2.find(',')
                n = line2.find(',',m+1)
                t = line2.find(',',n+1)
                label2 = line2[0:m]
                start2 = line2[m+1:n]
                end2 = line2[n+1:t] 
                if label == label2 :
                    IoU = IOU(float(start), float(end), float(start2), float(end2))                   
                    if IoU > 0.5 : #设定阈值
                        f = open('recall-mark.txt', 'a')
                        f.writelines(line2)
                        f.close() 
                        f = open('precision-mark.txt', 'a')
                        f.writelines(line)
                        f.close() 

print 'end....'
    
