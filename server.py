#!/usr/bin/env python3

import socket
import os 
import json
# from multiprocessing import Process
import threading
from config import method_table, expected_types, methods_info

def can_be_converted(params, expected_types):
    for i, param in enumerate(params):
        try:
            expected_types[i](param)
        except ValueError:
            return False
    return True

def handle_client(client_socket, client_id):
    print(f'Sending methods info to client {client_id}')
    client_socket.sendall(json.dumps(methods_info).encode())

    try:
        while True:
            data = client_socket.recv(1024)
            print(f'Received from client {client_id}: {data.decode()}')

            if data:
                request = json.loads(data)
                method = request['method']
                params = request['params']

                # Check if the method exists
                if method in method_table:
                    # Check if the parameters can be converted to the correct types
                    if can_be_converted(params, expected_types[method]):
                        # Convert the parameters to the correct types
                        params = [expected_types[method][i](param) for i, param in enumerate(params)]
                        # Call the method
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
            else:
                print(f'No data from the client {client_id}')
                break
    finally:
        print(f'Closing connection with client {client_id}')
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    socket_path = '/tmp/echo.sock'

    try:
        os.unlink(socket_path)
    except FileNotFoundError:
        pass

    server_socket.bind(socket_path)
    server_socket.listen(3)

    try:
        client_id = 0
        while True:
            print('Waiting for a connection...')
            client_socket, _ = server_socket.accept()
            print(f'Accpeted connection from client {client_id}')
            # Process(target=handle_client, args=(client_socket, client_id)).start()
            threading.Thread(target=handle_client, args=(client_socket, client_id)).start()
            client_id += 1
    except KeyboardInterrupt:
        print('Closing server...')
        server_socket.close()

if __name__ == '__main__':
    main()