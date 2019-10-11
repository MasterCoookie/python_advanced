'''
The example of TCP connection. This protocole is slower bcs it chcecks
whether data recieved is intact. Used where all the data is necessary
ex web pages.
'''

import socket

def main():
    '''The main function.'''
    host = '127.0.0.1'
    port = 5000

    sck = socket.socket()
    sck.bind((host, port))

    sck.listen(1)
    client, addr = sck.accept()
    print("Connection from:", addr)
    while 1:
        data = client.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user:", data)
        data = data.upper()
        print("Sending:", data)
        client.send(data.encode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()
