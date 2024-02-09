import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 12345)
server_socket.bind(address)

print("Server is starting with ", server_socket.connect_ex)

server_socket.listen(5)  # number of connections
print("Server Started Listening on ", address)
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}. ")
    data = client_socket.recv(1024)  # can recieve upto 1024 bytes of data
    print(f"Client : {data.decode()}")
    response = input()
    client_socket.send(response.encode())
    client_socket.close()

else:
    server_socket.close()
