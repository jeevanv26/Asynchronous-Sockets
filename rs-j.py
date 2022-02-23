import socket
import select


def server():
    try:
        rs= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()


    server_binding = ('', 50010)
    rs.setblocking(0)
    rs.bind(server_binding)
    rs.listen(2)
    host = socket.gethostname() #local host name
    localhost_ip = (socket.gethostbyname(host))
    csockid, addr = ss.accept()

    print("[RS]: Server host name is {}".format(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    print ("[RS]: Got a connection request from a client at {}".format(addr)

    # Define the port on which you want to connect to the server
    TS1port = 50011
    TS1host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS1_binding = (TS1host_addr, TS1port)
    ts1.connect(TS1_binding)

    TS2port = 50012
    TS2host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS2_binding = (TS2host_addr, TS2port)
    ts2.connect(TS2_binding)


   

    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[RS]: received data from client")
        ts1.send(data.encode())
        ts2.send(data.encode())
        print(" sent data to servers")
