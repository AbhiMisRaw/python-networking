import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ("127.0.0.1", 12345)

udp_server.bind(address)
print(f"Server listening to : {address}")

while True:
    # Recieve data from client
    data, client_address = udp_server.recvfrom(1024)
    print(f"Client: {data.decode()} -by {client_address}")

    response = input()
    udp_server.sendto(response.encode(), client_address)
