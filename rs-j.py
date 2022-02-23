import socket
import select
import sys


def server():
    try:
        rs= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()


    server_binding = ('', 50021)
    #rs.setblocking(0)
    rs.bind(server_binding)
    rs.listen(2)
    host = socket.gethostname() #local host name
    localhost_ip = (socket.gethostbyname(host))
    csockid, addr = rs.accept()

    print("[RS]: Server host name is {}".format(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    print("[RS]: Got a connection request from a client at {}".format(addr))

    # Define the port on which you want to connect to the server
    TS1port = 50011
    TS1host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS1_binding = (TS1host_addr, TS1port)
    ts1.connect(TS1_binding)

    TS2port = 50012
    TS2host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS2_binding = (TS2host_addr, TS2port)
    ts2.connect(TS2_binding)
    sockets = [ts1, ts2]


    while(True):
        data = csockid.recv(1024)
        #data = csockid.recv(1024)
        if not data: break
        print("[RS]: received data from client {}".format(data))
        ts1.send(data.encode())
        ts2.send(data.encode())
        readable, writable, errors = select.select(sockets,[], [], 5)
        if not readable:
            timeout = data + "  -  TIMED OUT"
            csockid.send(timeout)
        if readable:
            for r in readable:
                if r is ts1:
                    csockid.send(ts1.recv(1024))
                elif r is ts2:
                    csockid.send(ts2.recv(1024))



if __name__ == '__main__':
    server()
