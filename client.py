#!/usr/bin/env python3

import socket 

def    start_tcp_client():
       client_socket = socket.socket (socket.AF_INET, socket. SOCK_STREAM)
       client_socket.connect (('localhost', 8080))
       massage = client_socket.recv (1024)
       print (f"Received from server :{massage.decode()}")
       client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
