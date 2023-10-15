import os
import socket

def receive_file(sock, file_name):
    with open("./clientfolder/" + file_name, "wb") as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"File {file_name} received successfully.")

def send_message(sock, message):
    sock.sendall(message.encode())

def receive_message(sock):
    message = sock.recv(1024).decode()
    print(f"Received message: {message}")

host = input("Enter host name: ")
#ipv4 and tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, 22207))
    print("Connected")
except Exception as e:
    print(f"Not able to connect: {e}")
    exit(0)

# Example of receiving a message prefixed with 'MSG:'
data_type = sock.recv(4).decode()

if data_type == 'FILE':
    file_name = sock.recv(1024).decode()
    receive_file(sock, file_name)
elif data_type == 'MSG:':
    receive_message(sock)
else:
    print("Unknown data type received.")

sock.close()
