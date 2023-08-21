import socket


def handle_request(client_socket, request_data):
    # Process the request data and prepare a response
    response_content = "Hello, this is a simple HTTP server!"
    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_content)}\r\n\r\n{response_content}"
    client_socket.sendall(response.encode())
    client_socket.close()


def main():
    server_host = "127.0.0.1"
    server_port = 8080

    # Create a socket and bind it to the server address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from: {client_address[0]}:{client_address[1]}")

        request_data = client_socket.recv(1024).decode()
        if request_data:
            print("Received request:")
            print(request_data)
            handle_request(client_socket, request_data)
        else:
            print("No data received")


if __name__ == "__main__":
    main()
