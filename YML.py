# -*- coding: utf-8 -*-

__author__='yml'

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
        data.append([float(x) for x in line.split()])
        line=file.readline()
    return data

def str2float(list):
    return map(float,list)

