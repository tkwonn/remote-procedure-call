import socket
import os
import json
import select
from config import method_table, expected_types, methods_info

def can_be_converted(params, expected_types):
    for i, param in enumerate(params):
        try:
            expected_types[i](param)
        except ValueError:
            return False
    return True

def handle_request(client_socket, client_id):
    data = client_socket.recv(1024)
    if not data:
        print(f'Client {client_id} disconnected')
        return False

    print(f'Received from client {client_id}: {data.decode()}')

    try:
        request = json.loads(data)
        method = request['method']
        params = request['params']

        if method in method_table:
            if can_be_converted(params, expected_types[method]):
                params = [expected_types[method][i](param) for i, param in enumerate(params)]
                result = method_table[method](*params)
                message = {
                    'id': client_id,
                    'result': result,
                    'return type': type(result).__name__
                }
            else:
                message = {
                    'id': client_id,
                    'error': 'Invalid parameter'
                }
        else:
            message = {
                'id': client_id,
                'error': 'Method not found'
            }

        response = json.dumps(message).encode()
        print(f'Sending >>>>> {response.decode()}\n')
        client_socket.sendall(response)
    except json.JSONDecodeError:
        print(f'Invalid JSON from client {client_id}')
        client_socket.sendall(json.dumps({'error': 'Invalid JSON format'}).encode())
    return True

def main():
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    socket_path = '/tmp/echo.sock'

    try:
        os.unlink(socket_path)
    except FileNotFoundError:
        pass

    server_socket.bind(socket_path)
    server_socket.listen(5)

    print('Server started, waiting for connections...')

    inputs = [server_socket]
    clients = {}
    next_client_id = 0  # Keep track of the next client ID

    try:
        while True:
            readable, _, _ = select.select(inputs, [], [])

            for sock in readable:
                if sock is server_socket:
                    client_socket, _ = server_socket.accept()
                    inputs.append(client_socket)
                    clients[client_socket] = next_client_id  # Assign a unique ID
                    print(f'Accepted connection from client {next_client_id}')
                    client_socket.sendall(json.dumps(methods_info).encode())
                    next_client_id += 1
                else:
                    client_id = clients.get(sock, -1)  # Retrieve the client ID
                    if client_id == -1:
                        print('Error: Client not recognized')
                        continue
                    if not handle_request(sock, client_id):
                        inputs.remove(sock)
                        del clients[sock]
                        sock.close()
    except KeyboardInterrupt:
        print('Shutting down server...')
    finally:
        server_socket.close()
        os.unlink(socket_path)

if __name__ == '__main__':
    main()
