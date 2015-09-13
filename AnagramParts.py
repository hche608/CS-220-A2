#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys

def main(ss):
    res = dict()
    for s in ss:
        res[s] = sorted(s)
    pre_key = None
    for v in sorted(res, key=res.get, reverse=True):
        if pre_key == None:
            pre_key = sorted(v)
        if sorted(v) == pre_key:
            print(v)
        else:            
            print("\n",v)
        pre_key = sorted(v)           
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        print(main(d.split(' ')))
        print("\n")