from socket import *
 
def Main():
        host = '127.0.0.1'
        port = 9500
         
        s= socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
         
        message = input(" -> ")
         
        while True:
                s.send(message.encode())
                data = s.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        s.close()
 
if __name__ == '__main__':
    Main()