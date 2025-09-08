import socket
import sys
import time

new_socket = socket.socket() #create socket
host = socket.gethostname() #retrieve local device name 
socket_ip = socket.gethostbyname(host) # retrieves ip of other user
port = 8080

new_socket.bind((host, port))
print("Binding was a success.")
print("This is your ip: ", socket_ip)


name = input("Enter your name:")
new_socket.listen(1)

connection, add = new_socket.accept() #connection is connected to the socket and add is assigned to the IP address of the client
print("Connection from: " , add[0])
print("Connection established with: ", add[0])

client = (connection.recv(1024)).decode()
print(client + " connected.")
connection.send(name.encode())

while True:
    message = input("Enter message: ") #user sends message then waits for returning message
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client, ":", message) 