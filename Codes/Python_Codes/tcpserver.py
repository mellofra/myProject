#!/usr/bin/python

'''
Author: Nicolas Mello Franca
Function: Simple TCP server
Date: 09/09/2017
'''

import socket

try:

	ip = '0.0.0.0'
	port = 9999

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.bind((ip, port))

	server.listen(5)

	while True:

		con, cliente = server.accept()
		print '[*] Conectando por {0}'.format(cliente[0])

		msg = con.recv(1024)
		if not msg: break
		print cliente, msg

		print '[*] Finalizando com o cliente {0}'.format(cliente[0])
		server.close()

except KeyboardInterrupt as koi:
	print "[*] Connection closed"
	server.close()
