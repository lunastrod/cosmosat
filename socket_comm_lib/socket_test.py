# echo-server.py

import socket

import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("socket created")
    s.bind((HOST, PORT))
    print("bind")
    s.listen()
    conn, addr = s.accept()
    print("accept")
    with conn:
        print(f"Connected by {addr}")
        while True:
            print("recv")
            #x = YourStruct()
            data = conn.recv(4)
            #print(struct.calcsize(uplink_msg_order))
            #print(struct.unpack(uplink_msg_order, data))
            print(data)
            if not data:
                break
            
            conn.sendall(encode_downlink_msg("hola soy el servidor\n\0"))
            time.sleep(1)
            

    


