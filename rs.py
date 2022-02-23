import socket
import select




def server():
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[RS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    rs.setblocking(0)

    # Bind the socket to the port
    rs = ('', 50015)
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(5)

    inputs = [rs]
    outputs = []
    messages = {}

    while inputs:
        readable, writable, errors = select.select(inputs, outputs, [], 5)

        if readable or writable
            for r in readable:
                if r is rs:
                    conn, add = r.accept()
                    conn.setblocking(0)
                    input.append(conn)
                else:
                    data = r.recv(200)
                    outputs.append(r)
                    messages[r] = "Successful"
                    inputs.remove(r)

            for w in writable:
                msg = messages[w]
                w.send(msg)
                outputs.remove(w)

        else:
            rs.close()
            input.remove(TS1)
            input.remove(TS2)
