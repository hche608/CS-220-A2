#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import operator
import socket

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
    pre_key = None
    for k, v in sorted(res.items(),key=operator.itemgetter(1)):
        if k != '' and v != '':
            print(' '.join(v)) 

def send_data_tcp(message):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect the socket to the port where the server is listening
        sock.connect(('115.188.34.161', 10000))
   
        # Send data
        sock.send(bytes(message, 'UTF-8'))
    except socket.error:
    sock.close()    
            
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split('\n')
    for d in data:
        if d != '':
            anagram(d.split(' '))
            print()
    send_data_tcp(input)        