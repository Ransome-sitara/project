#!/usr/bin/env python3
import threading
import socket
host = '192.168.51.35'
port =  8080
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(( host, port))
server.listen()
clients = []
nicknames = []


def broadcast(message):
	for client in clients:
		client.send(message)

#functions to handle clients' connections


def handle_client(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} has left the  chat room! '. encode ('utf-8'))
			nicknames.remove(nickname)
			break
#main funtion to receive the clients connection


def receive():
	while True:
		print ('server is running and listening...')
		client, address = server.accept()
		print (f'connection is established with, {str (address)}')
		client.send('nickname?'.encode('utf-8'))
		nickname = client.recv(1024)
		nicknames.append(nickname)
		clients.append(client)
		print (f'the nickname of this client is {nickname} ' .encode('utf-8'))
		broadcast(f'{nickname} has connected to the chat room '.encode('utf-8'))
		client.send('you are now connected!' .encode('utf-8'))
		thread = threading.Thread(target = handle_client, args = (client,))
		thread.start()


if __name__ == "__main__":
	receive()
