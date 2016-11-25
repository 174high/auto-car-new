import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("192.168.3.100",8000);
sock.bind(server_address)
sock.listen(1)

while True:

    print "waiting for connection"
    connection,client_address=sock.accept()
    print  "Connection from: ", client_address 


#server_socket = socket.socket()
#server_socket.bind(('192.168.3.100', 8000))
#server_socket.listen(0)                                        
#connection, client_address =server_socket.accept()
#connection = connection.makefile('rb')

#print "Connection from: ", client_address

while True:
    data=connection.read(1)
    print data

