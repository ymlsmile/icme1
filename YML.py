# -*- coding: utf-8 -*-

__author__='yml'

def writelist(filename,list):
    with file(filename + '.txt', 'w+') as f:
        for data in list:
            k = ' '.join([str(j) for j in data])
            f.write(k + "\n")


def readlist(filename):
    with open(filename) as file:
        data = []
        line = file.readline()
        while line:
            data.append([float(x) for x in line.split()])
            line = file.readline()
    return data

def str2float(list):
    return map(float,list)

