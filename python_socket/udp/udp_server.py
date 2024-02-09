import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ("127.0.0.1", 12345)
server_socket.bind(address)

data, client_address = server_socket.recvfrom(1024)

print(f"Recieved : {data} by-{client_address}")
