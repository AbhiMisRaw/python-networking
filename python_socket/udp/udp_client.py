import socket

# here we'r sending data to UDP server -> socket.SOCK_DGRAM
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Write message to send UDP Server")
data = input()

server_address = ("127.0.0.1", 12345)

# bcz udp is connection less protocol don't need to connect to udp server

client_socket.sendto(data.encode(), server_address)
# here we will send data using sendto() which takes data and server address as arguments

response, server_address = client_socket.recvfrom(1024)

print(f"Server : {response.decode()} -by {server_address}")

client_socket.close()
