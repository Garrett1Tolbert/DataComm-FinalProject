#!/usr/bin/env python
import time
import socket

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# request sent to server
send_time_ms = time.time()

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print('Received Data:\n%s'% (data))
        break
        if not data:
            f.close()
            print 'file close()'
            break
        # write data to a file
        f.write(data)

# response sent from server
recv_time_ms = time.time()
rtt_in_ms = round(recv_time_ms - send_time_ms, 6)

print('RTT: ' + str(rtt_in_ms))
s.close()
print('connection closed')
