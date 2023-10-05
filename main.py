import socket
import os
import time

# Opção 1: Servidor Web Simples
def run_web_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 80))
    server_socket.listen(1)

    print("Servidor Web: Aguardando conexão...")
    connection, address = server_socket.accept()

    request = connection.recv(1024).decode()
    filename = request.split()[1][1:]

    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\n\r\n".encode() + content
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode() + b"404 Not Found"

    connection.send(response)
    connection.close()

# Oppção 2: Cliente Ping UDP
def run_udp_ping_client():
    server_address = ('localhost', 12000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(1, 11):
        message = f'Ping {i}'.encode()
        start_time = time.time()
        client_socket.sendto(message, server_address)

        try:
            client_socket.settimeout(1)
            response, server = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = end_time - start_time
            print(f'Cliente Ping UDP: Received: {response.decode()}, RTT: {rtt} seconds')
        except socket.timeout:
            print(f'Cliente Ping UDP: Ping {i} Request Timed Out')

    client_socket.close()

if __name__ == '__main__':
    
    task = input("Digite '1' para Servidor Web ou '2' para Cliente Ping UDP: ")
    
    if task == '1':
        run_web_server()
    elif task == '2':
        run_udp_ping_client()
    else:
        print("Escolha inválida. Digite '1' ou '2'.")
