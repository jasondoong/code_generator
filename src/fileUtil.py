'''
Created on 2014/7/23

@author: jason
'''
def readfile(path):
    out = []
    f = open(path, 'r')
    for line in f:
        out.append(line)
    return out