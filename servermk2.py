
import time
import socket
import threading



port = 8080
clients = []
users = {}
clients_lock = threading.Lock()
users_lock = threading.Lock() #some thread locks to ensure clients arent iterating, modifying, etc clients and users at the same time

#checks if message is a string, if so, sends if fails removes client from list
def send_message(client, message): 
    if isinstance(message, str):
        message = message.encode()
    try:
        client.sendall(message)
    except Exception as e:
        print("send_message failed:", e)
        remove_client(client)

def remove_client(client):
    with clients_lock:
        if client in clients:
            clients.remove(client)
    with users_lock:
        if client in users:
            del users[client]
    try:
        client.close()
    except:
        pass

#send the message to everone nut sender
def broadcast(msg, client_socket=None):
    with clients_lock:
        for client in clients:
            
            if client != client_socket:
                
               send_message(client, msg)


def client_handler(connection, address):
    try:
        broadcast(f"Connection from: {address[0]}", connection)
        
        username = connection.recv(1024).decode()
        print(f"Connection from: {address[0]} '{username}'")
        users[connection] = username

        while True:
            
            message = connection.recv(1024).decode()
            split_message = message.split(" ", 2)
            if split_message[0] == "users":
                chat_commands(message, connection)
            if split_message[0] == "ping":
                chat_commands(message, connection)
            if split_message[0] == "msg":
                chat_commands(message, connection)
            else:
                broadcast((time.strftime("%H:%M:%S", time.localtime()) +" " + username +": " + message).encode(), client_socket=connection)
                print(username +": " + message)

            

    except:
        pass
            

def chat_commands(command=None, connection=None):
    command = command.split(" ", 2)
    print (connection)
    
    if command[0] == "users":
        with users_lock:

            user_list = [user for user in users.values()]
        message = "users:\n" +"\n".join(user_list)
        print(message)
        send_message(connection, message)
    if command[0] == "msg":
        with users_lock:
            username = command[1]
            target = next((t for t, u in users.items() if u == username), None)
            print (target)
            send_message(target, f"Private message from {users.get(connection)}: {command[2]}")
    if command[0] == "ping":
        send_message(connection, "pong")
        
          




def main():
    server_socket = socket.socket()
    server_ip = socket.gethostbyname(socket.gethostname())
    server_socket.bind((server_ip, port))
    server_socket.listen()
    
    
    while True:
        
        print("Server started! Waiting for connections...")
        
        conn, addr = server_socket.accept()
        clients.append(conn)
        threading.Thread(target=client_handler, args=(conn, addr), daemon=True).start()
       ## threading.Thread(target=chat_commands).start()
        
    
    
if __name__ == "__main__":
    main()
    
