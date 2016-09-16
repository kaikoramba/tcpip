import sys
import socket
import time

bufsize = 1024

def printf(word):
    print word
    sys.stdout.flush()

def tcp_server(host,port,sock_name):
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock0.bind((host, port))
    sock0.listen(1)
    printf(sock_name+':waiting for connection...')
    (sock, client_addr) = sock0.accept()
    printf(sock_name+':connection start')
    return sock

def tcp_client(host,port,sock_name,retry_sec):
    while True:
        printf(sock_name+":connecting to %s, port:%s" % (host, port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
            printf('connected')
            return sock
        except socket.error as e:
            printf(sock_name+":fail to connect, wait for %dsec" % retry_sec)
            time.sleep(retry_sec)

def tcp_send(sock,msg):
    try:
        sock.send(msg)
    except socket.error as e:
        printf("connection closed")
        return -1
    return 0

def tcp_receive(sock):
    try:
        msg = sock.recv(bufsize)
        msg = msg.rstrip()

        if msg == "":
            printf('connection end')
            return -1
        else:
            # printf("received : %s" % msg)
            return msg
    except socket.error as e:
        printf("connection closed")
        return -1

def check_status(sock,list_status,list_trigger):
        sock.send('S\n')
        status = tcp_receive(sock)
        if status == -1:
            return -1
        elif status in list_trigger:
            return 1
        elif status not in list_status:
            printf('unexpected pc_status:'+pc_status)
            return -1
        else:
            return 0
