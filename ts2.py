import threading
import time
import random

import socket

def ts1():
    try:
        ts2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    ts2_binding = ('', 50011)
    ts2.bind(ts2_binding)
    ts2.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ts2.accept()
    print ("[S]: Got a connection request from a root at {}".format(addr))

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
            dictionary[key] = value


    #receive data from root server and send back ip if exists
    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[TS1]: received data from root server")
        if(data in dictionary):
            csockid.send(dictionary[data].encode('utf-8'))



    ts2.close()
    exit()