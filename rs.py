import socket
import select




def server():
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[RS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    TS1port = 50011
    TS1host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS1_binding = (TS1host_addr, TS1port)
    TS1.connect(TS1_binding)

    TS2port = 50012
    TS2host_addr = socket.gethostbyname(socket.gethostname()) #local host name
    TS2_binding = (TS2host_addr, TS2port)
    TS2.connect(TS2_binding)

    server_binding = ('', 50010)
    rs.setblocking(0)
    rs.bind(server_binding)
    rs.listen(2)
    host = socket.gethostname() #local host name
    localhost_ip = (socket.gethostbyname(host))
    csockid, addr = ss.accept()

    print("[RS]: Server host name is {}".format(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    print ("[RS]: Got a connection request from a client at {}".format(addr))


    alldata = [] #from client
    while(True):
        data = csockid.recv(1024)
        if not data: break
        print("[RS]: received data from client")
        alldata.append(data)
    print(alldata)

    inputs = [TS1, TS2]
    outputs = []
    messages = {}
    counter = 0

    while inputs:
        readable, writable, errors = select.select(inputs, outputs, [], 5)

        if readable or writable
            for r in readable:
                if r is TS1 or TS2: #accept all sockets
                    conn, add = r.accept()
                    conn.setblocking(0)
                    input.append(conn)
                else: #data gets thrown into RS to read
                    data = r.recv(200)
                    outputs.append(r)
                    print("[S]: Server got {} from TS".format(data))
                    messages[r] = data
                    inputs.remove(r)

            for w in writable: #
                msg = alldata[counter]
                w.send(msg)
                outputs.remove(w)
                counter+=1

        else:
            rs.close()
            input.remove(TS1)
            input.remove(TS2)
