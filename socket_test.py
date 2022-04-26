"""
#!/usr/bin/env python

import sys
import ctypes
import struct


class YourStruct(ctypes.Structure):
    _fields_ = [
        ("v", ctypes.c_float),
        ("t", ctypes.c_int),
        ("c", ctypes.c_char),
    ]


def main(*argv):
    data = b"\x9a\x99\x99?*\x00\x00\x00A\xbe\xad\xde"
    x = YourStruct()
    fmt = "<fic"
    fmt_size = struct.calcsize(fmt)
    x.v, x.t, x.c = struct.unpack(fmt, data[:fmt_size])
    print("Fields\n  v: {:f}\n  t: {:d}\n  c: {:s}".format(x.v, x.t, x.c.decode()))


if __name__ == "__main__":
    print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main(*sys.argv[1:])
    print("\nDone.")

"""

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
            

