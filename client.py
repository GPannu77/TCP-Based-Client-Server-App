
"""
client.py: Multi-Service TCP Client

Using: python3 client.py
Connects to the server at HOST:PORT below and lets you send as many 
CONVERT requests as you want, one per line, until you type QUIT.
"""

import socket

HOST = "127.0.0.1"
PORT = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
client_file = client_socket.makefile("r")

print(f"Connected to server at {HOST}: {PORT}")
print("Type a request, e.g. CONVERT TEMP C F 25")
print("Type QUIT to exit.")

while True:
    request = input("> ").strip()
    
    if not request:
        continue
    
    client_socket.sendall(request.encode()+ b"\n")
    
    if request.upper() == "QUIT":
        break
    
    response = client_file.readline().strip()
    print(response)
    
client_socket.close()
print("Connection closed.")