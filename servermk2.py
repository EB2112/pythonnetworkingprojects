
import time
import socket
import threading



port = 8080
clients = []
users = {}


def send_message(msg, client_socket):
    for client in clients:
        
        if client != client_socket:
            print(client)
            try:
                client.sendall(msg)
            except:
                pass


def client_handler(connection, address):
    try:
        send_message(f"Connection from: {address[0]}", connection)
        print(f"Connection from: {address[0]}")
        username = connection.recv(1024).decode()
        users[connection] = username

        while True:
            
            message = connection.recv(1024).decode()
            if message == "stop":
                break
            
            send_message((username +": " + message).encode(), connection)
            print(username +": " + message)

    except:
            pass
            




def main():
    server_socket = socket.socket()
    server_ip = socket.gethostbyname(socket.gethostname())
    server_socket.bind((server_ip, port))
    server_socket.listen()
    while True:
        print("on")
        conn, addr = server_socket.accept()
        clients.append(conn)
        print(clients)
        threading.Thread(target=client_handler, args=(conn, addr), daemon=True).start()
    
    
if __name__ == "__main__":
    main()
    
