import socket
import select




def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TS1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TS2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[RS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    TS1port = 50011
    TS1host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS1_binding = (TS1host_addr, TS1port)
    TSI.connect(TS1_binding)

    TS2port = 50012
    TS2host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS2_binding = (TS2host_addr, TS2port)
    TS2.connect(TS2_binding)


    server_binding = ('', 50010)
    ss.setblocking(0)
    ss.bind(server_binding)
    ss.listen(2)
    host = socket.gethostname() #local host name
    localhost_ip = (socket.gethostbyname(host))
    csockid, addr = ss.accept()

    print("[RS]: Server host name is {}".format(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    print ("[RS]: Got a connection request from a client at {}".format(addr))

    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[RS]: received data from client")
