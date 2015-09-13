#!/usr/bin/env python3
# A2 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import socket
import sys

def automarker_hacker():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 10000)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(5)
    
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print('received:\n %s' % data)
                if not data:
                    break
            
        finally:
            # Clean up the connection
            connection.close()
        
if __name__ == '__main__':
    automarker_hacker()
