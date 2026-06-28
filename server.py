"""
server.py: Multi-Service TCP Server

Using: python3 server.py 
Port: 9000

Listens to a specified port and handles each client
connection in its own thread, so multiple clients can 
be served simultaneously.
"""
import socket
import threading



HOST = "0.0.0.0"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

def process_request(line):
    tokens = line.split()
    
    if len(tokens) != 5 or tokens[0].upper() != "CONVERT":
        return "ERROR Malformed request"
    
    category = tokens[1].upper()
    from_type = tokens[2].upper()
    to_type = tokens[3].upper()
    value_str = tokens[4]
    
    try:
        value = float(value_str)
    except ValueError:
        return "ERROR Invalid numeric value"
    
    if category == "TEMP":
        if from_type == to_type:
            result = value
        elif from_type == "C" and to_type =="F":
            result = (value * 9/5) + 32
        elif from_type == "F" and to_type == "C":
            result = (value - 32) * 5/9
        else:
            return "ERROR Invalid unit"
        return f"RESULT {result:.2f} {to_type}"
    
    elif category == "CURRENCY":
        
        if from_type == to_type:
            result = value
        elif from_type == "USD" and to_type == "EUR":
            result = value * 0.88
        elif from_type == "EUR" and to_type == "USD":
            result = value * 1.14
        elif from_type == "USD" and to_type == "GBP":
            result = value * 0.76
        elif from_type == "GBP" and to_type == "USD":
            result = value * 1.32
        elif from_type == "USD" and to_type == "CAD":
            result = value * 1.37
        elif from_type == "CAD" and to_type == "USD":
            result = value * 0.73
        elif from_type == "EUR" and to_type == "GBP":
            result = value * 0.86
        elif from_type == "GBP" and to_type == "EUR":
            result = value * 1.16
        elif from_type == "EUR" and to_type == "CAD":
            result = value * 1.62
        elif from_type == "CAD" and to_type == "EUR":
            result = value * 0.62
        elif from_type == "GBP" and to_type == "CAD":
            result = value * 1.87
        elif from_type == "CAD" and to_type == "GBP":
            result = value * 0.53
        else:
            return "ERROR Invalid unit"
        return f"RESULT {result:.2f} {to_type}"
    
    elif category == "LENGTH":
        
        if from_type == to_type:
            result = value
        elif from_type == "KM" and to_type == "MI":
            result = value * 0.621371
        elif from_type == "MI" and to_type == "KM":
            result = value * 1.60934
        else:
            return "ERROR Invalid unit"
        return f"RESULT {result:.2f} {to_type}"
    
    elif category == "WEIGHT":
        
        if from_type == to_type:
            result = value
        elif from_type == "KG" and to_type == "LB":
            result = value * 2.20462
        elif from_type == "LB" and to_type == "KG":
            result = value * 0.453592
        else:
            return "ERROR Invalid unit"
        return f"RESULT {result:.2f} {to_type}"
    else:
        return "ERROR Invalid category"
        

def handle_client(connection, address):
    print(f"Connected by {address}")
    connection_file = connection.makefile("r")
    
    for line in connection_file:
        line2 = line.strip()
        if not line2:
            continue
        if line2.upper() == "QUIT" or line2.upper() == "EXIT":
            print(f"Client {address} requested to quit.")
            break
        
        response = process_request(line2)
        connection.sendall(response.encode() + b"\n")
    
    connection.close()
    print(f"Connection with {address} now closed.")


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

