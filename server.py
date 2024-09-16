#!/usr/bin/env python3
import socket

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print ("TCP server listening on port 8080")

    while True:
          client_socket,client_address = server_socket.accept()
          print (f"connection established with {client_address}")
          client_socket.send (b'Hello from TCP sever ! ')
          client_socket.close()

if __name__ == "__main__":
    start_tcp_server()

