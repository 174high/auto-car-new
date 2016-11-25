import socket
import time 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.3.101', 8000))
connection = client_socket.makefile('wb')

print "----connection--- :"

while True: 

    connection.write("a")
    connection.flush()
    time.sleep(1)


