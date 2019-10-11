import socket

def main():
    '''The main function.'''
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1', 5000)

    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sck.bind((host, port))

    msg = input("-> ")
    while msg != 'q':
        sck.sendto(msg.encode('utf-8'), server)
        data, addr = sck.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recieved from server:", data)
        msg = input("-> ")
    sck.close()

if __name__ == '__main__':
    main()
