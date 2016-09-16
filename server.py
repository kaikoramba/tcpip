import sys,socket
from util import *

host = "127.0.0.1"
port = 1111

sock = tcp_server(host,port,"server")

while True:
    data = tcp_receive(sock)
    if data == -1:
        break
    printf(data)
    ret = 'OK:' + data
    sock.send(ret)

sock.close()
