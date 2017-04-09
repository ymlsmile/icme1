# -*- coding: utf-8 -*-
import os
  
dir=r"D:\g470\icme\data\Train_Label_PKU--test"
m = 0
for root,dirs,files in os.walk(dir):
    for file in files:
        filename = os.path.join(file)
        label_filename = dir + '/' + filename
    #    print label_filename    
        file1 = open(label_filename) 
        i = float(len(file1.readlines()))
        file1.close() 
        m = m + i 
print m
file2 = open('recall-mark.txt') 
n = float(len(file2.readlines()))
file2.close() 
print n

recall = n/m
print 'recall = ' , recall

dir=r"D:\g470\icme\data\labels"
x = 0
for root,dirs,files in os.walk(dir):
    for file in files:
        filename = os.path.join(file)
        label_filename = dir + '/' + filename
     #   print label_filename    
        file1 = open(label_filename) 
        j = float(len(file1.readlines()))
        file1.close() 
        x = x + j 
print x

file2 = open('precision-mark.txt') 
y = float(len(file2.readlines()))
file2.close() 
print y

precision = y/x
print 'precision = ' , precision

F1 = 2 * (precision * recall) / (precision + recall)
print 'F1 = ', F1