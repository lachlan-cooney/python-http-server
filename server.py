import socket

# define the socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# create the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port {}'.format(SERVER_PORT))

while True:
    # wait for client connections
    client_connection, client_address = server_socket.accept()

    # get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # get the content of page/index.html
    fin = open('page/index.html')
    content = fin.read()
    fin.close()

    # send a HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# close the socket
server_socket.close()
