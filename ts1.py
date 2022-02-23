import threading
import time
import random

import socket

def ts1():
    try:
        ts1= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    ts1_binding = ('', 50011)
    ts1.bind(ts1_binding)
    ts1.listen(1)
    host = socket.gethostname()
    print("[TS2]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[TS2]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ts1.accept()
    print ("[TS2]: Got a connection request from a root at {}".format(addr))

    #populate dictionary with hostnames and ip addresses
    dictionary = dict()
    file = open('PROJ2-DNSTS1.txt', 'r')
    list = file.read().split()
    index = 1
    key = ""
    value = ""
    for(i in list):
        if(index % 3 == 1):
            key = i ;
        elif(index % 3 == 2 ):
            value = i;
        else:
            dictionary[key] = key + value + i

        index++;

    
    #receive data from root server and send back ip if exists
    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[TS1]: received data from root server")
        if(data in dictionary):
            csockid.send(dictionary[data].encode('utf-8'))



    ts1.close()
    exit()

