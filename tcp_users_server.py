import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establishing tcp socket

    server_address = ("localhost", 12345) #establishing address
    server_socket.bind(server_address) #binding socket and port

    server_socket.listen(10) #incoming request maximum (11-th will go to queue)
    print("The served is launched and ready to receive connections...")

    messages = []
    while True: #endless cycle
        #connecting the client
        client_socket, client_address = server_socket.accept()
        print(f"User {client_address} has connected")

        #getting data from client and collecting it into a list
        data = client_socket.recv(1024).decode()
        messages.append(data)
        print(f"User {client_address} has sent the message: {data}")

        #sending message to client
        client_socket.send('\n'.join(messages).encode())

        client_socket.close()

if __name__ == "__main__":
    server()