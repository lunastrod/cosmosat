import socket
import select

import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)

DOWNLINK_STR_MAX_SIZE=4096

def encode_downlink_msg(s,size):
    #pad spaces in string
    s = s.ljust(size-1)
    s+='\0'
    s=s.encode()[:size]
    #print(s)
    #print(len(s))
    return s

def downlink_msg_generator(float31list,bool32list):
    global DOWNLINK_STR_MAX_SIZE
    if(len(float31list)!=31):#make sure it has 31 values
        print("error float31list size")
        if(len(float31list)>31):
            float31list=float31list[:31]
        while(len(float31list)<31):
            float31list.append(0)
        print(len(float31list))

    if(len(bool32list)!=32):#make sure it has 32 values
        print("error bool32list size")
        if(len(bool32list)>32):
            bool32list=bool32list[:32]
        while(len(bool32list)<32):
            bool32list.append(False)
        print(len(bool32list))
        
    bitfield_str=""
    for b in bool32list:
        if(b):
            bitfield_str+="1"
        else:
            bitfield_str+="0"

    float_str=""
    for n in float31list:                                                                                                                                                                               
        float_str=float_str+"{:.6f} ".format(n)
    
    msg=float_str+bitfield_str
    return encode_downlink_msg(msg,DOWNLINK_STR_MAX_SIZE)

class antenna_connection():
    def __init__(self, ip, port):
        #create a socket object
        self.sock = socket.socket()
        # Next bind to the port
        self.sock.bind((ip, port))
        print("socket binded to %s" %(port))
        # put the socket into listening mode
        self.sock.listen(5)
        # Establish connection with client.
        self.conn, addr = self.sock.accept()
        print ('Got connection from', addr )
    def recv_send(self,downlink_msg):
        self.conn.setblocking(0)
        ready = select.select([self.conn], [], [], 0.1)
        if ready[0]:
            data = self.conn.recv(4)
            print(data)

        print(downlink_msg)
        print(len(downlink_msg))
        self.conn.sendall(downlink_msg)

    DOWNLINK_STR_MAX_SIZE=4096

    

        
a=antenna_connection(HOST,PORT)
while(True):
    a.recv_send(downlink_msg_generator(list(range(31)),[True]*32))
    time.sleep(1)