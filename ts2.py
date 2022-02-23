import threading
import time
import random
import sys

import socket

def ts2():
    try:
        ts2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #populate dictionary with hostnames and ip addresses
    dictionary = dict()
    file = open('PROJ2-DNSTS2.txt', 'r')
    list = file.read().split()
    index = 1
    key = ""
    value = ""
    for i in list:
        if(index % 3 == 1):
            key = i ;
        elif(index % 3 == 2 ):
            value = i;
        else:
            dictionary[key] = key + value + i

        index+=1

    ts2_binding = ('', 50012)
    ts2.bind(ts2_binding)
    ts2.listen(1)
    host = socket.gethostname()
    print("[TS2]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[TS2]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ts2.accept()
    print ("[TS2]: Got a connection request from a root at {}".format(addr))




    #receive data from root server and send back ip if exists
    result = ''
    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[TS2]: received data from root server")

        for key, value in dictionary.items():
            print(key, value)
            if data == key:
                csockid.send(value.encode('utf-8'))



    ts2.close()
    exit()

if __name__ == '__main__':
    ts2()
