# დავალება 2.

# სოკეტების გამოყენებით დაწერეთ ჩატი, სოკეტები უნდა 
# მოქმედებდეს TCP პროტოკოლით, სერვერის სოკეტს უნდა შეეძლოს 
# რექვესტების მიღება მხოლოდ ლოკალური ჰოსტიდან, მიმოწერა 
# შეინახეთ ტექსტურ ფაილში.


import socket
import threading

# სერვერის IP და PORT
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65535

# სერვერის სოკეტის შექმნა
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

# კლიენტების და ნიკნეიმების სიები
clients = []
nicknames = []

# ფაილის გახსნა, სადაც ჩაიწერება ჩატი
chat_log = open("chat_log.txt", "a")

# ფუნქცია, რომელიც ყველა კლიენტს უგზავნის შეტყობინებას
def broadcast(message):
    for client in clients:
        client.send(message)
    
    # შეტყობინების ჩაწერა ფაილში
    chat_log.write(message.decode() + "\n")
    chat_log.flush()  # დაუყოვნებლივ ჩაწერა ფაილში

# კლიენტის მიერ შეტყობინების მიღება და გადამუშავება
def handle(client):
    while True:
        try:
            # შეტყობინების მიღება კლიენტისგან
            message = client.recv(1024)
            # ყველა კლიენტს უგზავნის მიღებულ შეტყობინებას
            broadcast(message)
        except:
            # თუ კლიენტი გათიშულია, ამოიღე სიებიდან
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!!!".encode('utf-8'))
            nicknames.remove(nickname)
            client.close()
            break

# კავშირების მიღება კლიენტებისგან
def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected With {str(address)}")

        # ნიკნეიმის მოთხოვნა კლიენტისგან
        client.send("Nickname".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'{nickname} connected to the chat')
        broadcast(f"{nickname} has joined the chat!!!".encode('utf-8'))

        # ახალი თრედი კლიენტის დასამუშავებლად
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# კავშირის მიღების პროცესის დაწყება
receive()
