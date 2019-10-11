import socket

def main():
    '''The main function.'''
    host = '127.0.0.1'
    port = 5000

    sck = socket.socket()
    sck.connect((host, port))

    msg = input("-> ")
    while msg != 'q':
        sck.send(msg.encode('utf-8'))
        data = sck.recv(1024).decode('utf-8')
        print("Data recieved form server:", data)
        msg = input("-> ")
    sck.close()


if __name__ == '__main__':
    main()
