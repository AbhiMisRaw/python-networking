import socket


while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("127.0.0.1", 12345)

    client_socket.connect(server_address)
    print("Write Your message")
    data = input()
    if data == "quit":
        break
    client_socket.send(data.encode())
    response = client_socket.recv(1024)
    print(f"Server : {response.decode()}")
    client_socket.close()

print("Connection is terminated!")
print("------------EXIT---------------")
