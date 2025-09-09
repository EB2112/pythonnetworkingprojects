import socket
import sys
import time

socket_client = socket.socket()
port = 8080


server_host = input('Enter IP address you wish to connect to:')
name = input('Enter your name: ')
try: 
    socket_client.connect((server_host, port))
    socket_client.send(name.encode())
    server_name = socket_client.recv(1024).decode()
    print("hello ", server_name)

    while True:
        message = input("Enter message: ")
        if message.lower() == "/quit":
            break
        socket_client.send(message.encode())
        print(socket_client)

        server_name = socket_client.recv(1024).decode()
        server_message = socket_client.recv(1024).decode()
        
        print(server_message)
        
        if server_message.lower == "/quit":
            break
        print(server_name, ":", server_message)

except Exception as e:
    print("error occurred: " , e)

finally:
    socket_client.close()

