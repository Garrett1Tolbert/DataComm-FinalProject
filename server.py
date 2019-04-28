import socket
import os
import fnmatch
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = 'localhost'
# hostname-I and choose the longest value with letters and numbers
# it should be the 3rd or 4th value, which is the server address

# At any given time you're going to have 2 clients and one serverself.
# 2 client.py files with different TCP_IP

TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip_port,sock):
        Thread.__init__(self)
        self.ip_port = ip_port
        self.sock = sock
        print " New thread started for "+str(ip_port)

    def run(self):
        hasFile = False
        filename='mytext.txt'

        # checks if file is in current directory
        for file in os.listdir('/Users/gtolbert/Desktop/DataComm-FinalProject'):
            if fnmatch.fnmatch(file, filename):
                hasFile = True

        if hasFile == False :
            message = "Error:: file not found in directory"
            self.sock.send(message)
            self.sock.close()
        else:
            f = open(filename,'rb')
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    #print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break

tcpsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    (conn, ip_port) = tcpsock.accept()
    print 'Got connection from ', (ip_port)
    newthread = ClientThread(ip_port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
