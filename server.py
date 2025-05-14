# Name this file as server.py
# Import the socket module first.
import socket
# Create a socket object.
s = socket.socket()
# Get local machine name.
host = socket.gethostname()
# Reserve a port number for the service.
port = 123
# Bind to the port.
s.bind((host, port))
# Wait for a client connection.
# Here, 3 signifies that there can be maximum of 3 queued connections.
s.listen(3)
while True:
    # Establish a connection with the client.
    connection, address = s.accept()
    print('Received connection from', address)
    # Send a message to the client.
    connection.send(b'Thank you for connecting!')
    # Close the connection.
    connection.close()