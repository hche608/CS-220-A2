#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import socket

def idf(s, t):
        res = dict()
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = t[i]
            if res[s[i]] != t[i]:
                return False
        return True
        
# @param {string} s
# @param {string} t
# @return {boolean}        
def isIsomorphic(s, t):
    if len(s)!=len(t):
        return False    
    return idf(s, t) and idf(t, s)

def send_data_tcp(message):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    try:
        sock.connect(('115.188.34.161', 10000))   
        # Send data
        sock.send(bytes(message, 'UTF-8'))
    except socket.error:
        sock.close()  
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        res = d.split(' ')
        if (len(res) == 2):
            print(isIsomorphic(res[0], res[1]))
    send_data_tcp(input)          
