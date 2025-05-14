# Name this file as client.py
# Import the socket module first.
import socket
# Create a socket object.
s = socket.socket()
# Get local machine name.
host = socket.gethostname()
# Reserve a port number for the service.
port = 123
# Connect to the host on the given port.
s.connect((host, port))
# Receive data from the server.
print(str(s.recv(1024), 'utf-8'))
# Close the socket after completion.
s.close()
