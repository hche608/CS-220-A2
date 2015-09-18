#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import operator
import time

def anagram(data):
    res = dict()
    ss = sorted(data)
    for s in ss:
        key = ''.join(sorted(s))
        if not key in res.keys():
            res[key] = [s]
        else:
            res[key].append(s)
    pprint(res)       

def pprint(res):
    for k, v in sorted(res.items(),key=operator.itemgetter(1)):
        if k != '' and v != '':
            print(' '.join(v))   
            
if __name__ == '__main__':
    start = time.clock()
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        if d != '':
            anagram(d.split(' '))
            print() 
    elapsed = (time.clock() - start)
    #print("Time used:",elapsed*100)            