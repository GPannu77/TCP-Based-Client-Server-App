"""
server.py: Multi-Service TCP Server

Using: python3 server.py <port>

Listens to a specified port and handles each client
connection in its own thread, so multiple clients can 
be served simultaneously.
"""
import socket, threading



HOST = "0.0.0.0"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

def process_request(line):
    pass

def handle_client(connection, address):
    pass

def main():
    print(f"Server listening on port {PORT}...")
    try:
        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(connection, address))
            thread.start()
    except KeyboardInterrupt:
        print("\nServer closing...")
        server_socket.close()

if __name__ == "__main__":
    main()

