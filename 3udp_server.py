
# დავალება 3.

# მოიძიეთ ინფორმაცია UDP პროტოკოლის შესახებ და სცადეთ 
# ჩატის აწყობა მოცემული პროტოკოლის გამოყენებით

import socket

# სერვერის IP მისამართი და პორტი
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555

# UDP სოკეტის შექმნა
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

# ფაილის შექმნა ჩატის ლოგების შესანახად
chat_log = open("udp_chat_log.txt", "a")

while True:
    # შეტყობინების მიღება კლიენტისგან
    message, address = server_socket.recvfrom(1024)
    message_decoded = message.decode('utf-8')
    print(f"Received from {address}: {message_decoded}")

    # ჩატის ლოგის ფაილში ჩაწერა
    chat_log.write(f"{address}: {message_decoded}\n")
    chat_log.flush()  # დაუყოვნებლივ ჩაწერა ფაილში

    # პასუხის გაგზავნა კლიენტს
    server_socket.sendto(f"Received: {message_decoded}".encode('utf-8'), address)
