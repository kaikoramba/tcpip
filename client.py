import sys,socket
from util import *

host = '127.0.0.1'
port = 1111

def client():
    sock = tcp_client(host,port,"client",3)
    # sock.settimeout(1)
    try:
        while True:
            printf('input:')
            input_line = sys.stdin.readline()
            input_line = input_line.rstrip()
            sock.send(input_line)
            print tcp_receive(sock)
    except:
        sock.close()

if __name__ == "__main__":
	client()