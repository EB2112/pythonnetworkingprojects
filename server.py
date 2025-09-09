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




try:
    
    new_socket.listen(2)
    connection, addr = new_socket.accept()
    connection.send(name.encode())
    client = (connection.recv(1024)).decode()
    
    print(client + " connected.")
   


    while True:
        receiving_message = connection.recv(1024).decode()
        
        
        print(client, time.strftime("%d %b %Y %H:%M:%S ", time.localtime()),":", receiving_message) 

        message =  input("Enter message: ") #user sends message then waits for returning message
        if message.lower() == "/quit":
            break
        
        connection.send(name.encode())
        print(time.strftime("%d %b %Y %H:%M:%S", time.localtime()))
        connection.send(message.encode())
except Exception as e:
    print("error ", e)

finally:
    connection.close()
    new_socket.close()
