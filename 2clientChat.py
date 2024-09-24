import socket
import threading

# სერვერის IP და PORT
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65535

# კლიენტის სოკეტის შექმნა
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# სერვერისგან ნიკნეიმის მოთხოვნის მიღება
nickname = input("Choose your nickname: ")
client_socket.send(nickname.encode('utf-8'))

# შეტყობინებების მიღება სერვერისგან
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# შეტყობინებების გაგზავნა სერვერზე
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client_socket.send(message.encode('utf-8'))

# თრედი შეტყობინებების მისაღებად
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# თრედი შეტყობინებების გასაგზავნად
write_thread = threading.Thread(target=write)
write_thread.start()

