import socket
# კლიენტისთვის სოკეტის შექმნა
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# სერვერის მისამართთან დაკავშირება
client_socket.connect(('127.0.0.1', 65432))

# სერვერიდან მიღებული შეტყობინების დაბეჭვდვა
message = client_socket.recv(1024)
print(f"Message from server: {message.decode('utf-8')}")

client_socket.close()