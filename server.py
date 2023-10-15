import socket
import os

def send_file(client, file_name):
    
    client.sendall(b'FILE')
    client.sendall(file_name.encode())
    with open(file_name, "rb") as file:
        data = file.read(1024)
        while data:
            client.sendall(data)
            data = file.read(1024)
    print(f"File {file_name} sent successfully.")

def send_message(client, message):
    client.sendall(b'MSG:')
    client.sendall(message.encode())
    print("Message sent successfully.")

#AF_inet for ipv4 and sock stream for TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22207))
sock.listen(5)

print("HOST:", sock.getsockname())

client, adr = sock.accept()

choice = input("Do you want to send a file or a message? (file/message): ").lower()

if choice == 'file':
    file_name = input("Enter the file name: ")
    if os.path.exists(file_name):
        send_file(client, file_name)
    else:
        print("The specified file does not exist.")
elif choice == 'message':
    message = input("Enter the message: ")
    send_message(client, message)
else:
    print("Invalid option selected.")

client.close()
sock.close()


