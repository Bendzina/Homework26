import socket

# სერვერის IP და პორტი
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555

# UDP სოკეტის შექმნა
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nickname = input("Enter your nickname: ")

# შეტყობინებების გაგზავნის და მიღების პროცესი
while True:
    message = input(f"{nickname}: ")
    full_message = f"{nickname}: {message}"

    # შეტყობინების გაგზავნა სერვერზე
    client_socket.sendto(full_message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

    # სერვერის პასუხის მიღება
    response, _ = client_socket.recvfrom(1024)
    print(f"Server: {response.decode('utf-8')}")
