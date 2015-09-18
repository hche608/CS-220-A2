#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import time

def idf(s, t):
        res = dict()
        for i in range(len(s)):
            try:
                res[s[i]] = t[i]
            except KeyError:
                if res[s[i]] != t[i]:
                    return False
            #
            # if s[i] not in res:
            #     res[s[i]] = t[i]
            # else:
            #     if res[s[i]] != t[i]:
            #         return False
        return True
        
# @param {string} s
# @param {string} t
# @return {boolean}        
def isIsomorphic(s, t):
    if s == t:
        return True
    elif len(s)!=len(t):
        return False    
    return idf(s, t) and idf(t, s)
        
if __name__ == '__main__':
    start = time.clock()
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        res = d.split(' ')
        if (len(res) == 2):
            print(isIsomorphic(res[0], res[1]))            
    elapsed = (time.clock() - start)
    print("Time used:",elapsed*1000)