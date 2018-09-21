from socket import *
 
def Main():
    host = "127.0.0.1"
    port = 9500
     
    s = socket(AF_INET, SOCK_STREAM)
    print("Socket successfully created")
    s.bind((host, port))
    print("socket binded to %s" %(port))
    s.listen(5)
    print("socket is listening")
    conn, addr = s.accept()
    print('connected by', addr)
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            #data = str(data).upper()
            if(data == "Hello"):
                reply = "Hi"
            else:
                reply = "Goodbye"
            #print ("sending: " + str(reply))
            conn.send(reply.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()