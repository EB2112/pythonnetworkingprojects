import socket
import threading

host = "10.5.0.2"
port = 8080


username = input("Choose username: ")

client_socket = socket.socket()

def receive(socket):
    while True:
        try:
            message = socket.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break


client_socket.connect((host, port))
client_socket.sendall(username.encode())
threading.Thread(target=receive, args=(client_socket,), daemon=True).start()

while True:
    msg = input("Enter message: ")
    if msg.lower == "/quit":
        break
    
    client_socket.sendall(msg.encode())

client_socket.close()