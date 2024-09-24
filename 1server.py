# დავალება 1.

# სოკეტების გამოყენებით დაწერეთ კლიენტისა და სერვერის 
# მხარე, სოკეტები უნდა მოქმედებდეს TCP პროტოკოლის 
# გამოყენებით. სერვერის სოკეტს უნდა შეეძლოს რექვესტების 
# მიღება ნებისმიერი ჰოსტიდან. მაგალითისათვის კი სერვერის 
# კავშირის შექმნის დროს დაბეჭდეთ დაკავშირებული ჰოსტის 
# მისამართი და კლიენტის მხარეს გამოაგზავნეთ შეტყობინება 
# რომ კავშირი შედგა წარმატებით, დაბეჭდეთ კლიენტის მხარეს.
import socket
#სოკეტის შექმნა
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#აიპი მისამართის და პორტის მითითება
server_socket.bind(('0.0.0.0', 65432))
# სერვერის მოსმენა (როცა კავშირს ელოდება)
server_socket.listen(5)
print("server is listening...")

#კლიენტისგან კავშირის მიღება
while True:
    client_socket, address = server_socket.accept()
    print(f"Connected with {str(address)}")

    # კლიენტს უნდა გავუგზავნოთ შეტყობინება
    client_socket.send(b'Connection successful')
    
    # სოკეტის დახურვა
    client_socket.close()
  

   


