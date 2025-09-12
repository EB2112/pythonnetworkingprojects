import socket
import threading

host = "10.5.0.2"
port = 8080





def receive(socket):
    try:
        while True:
                message = socket.recv(1024)
                if not message:
                    break
                print(message.decode().strip())
    except Exception as e:
            print("receiver excepion", e)



def main():
    client_socket = socket.socket()
    client_socket.connect((host, port))
    username = input("Choose username: ")
    client_socket.sendall(username.encode())

    threading.Thread(target=receive, args=(client_socket,), daemon=True).start()
    try:
        while True:
            msg = input("Enter message: \n"  )
            client_socket.sendall(msg.encode())
    except KeyboardInterrupt:
         print("stopping")
    finally:
        client_socket.close()

    

if __name__ == "__main__":
     main()