import socket
import time

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50010
    host_addr = socket.gethostbyname(socket.gethostname()) #local host name

    # connect to the server on local machine
    server_binding = (host_addr, port)
    cs.connect(server_binding)

    # Send file lines to the server
    print("File")
    file = open('PROJ2-HNS.txt', 'r')
    output = open('RESOLVED.txt','w')
    lines = file.readlines()
    for line in lines:
        cs.send(line.encode())
        data = cs.recv(1024)
        output.write(data)
        print(data)
