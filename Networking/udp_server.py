'''
The example of UDP connection. Is faster than TCP becouse the connection
is direct and the data is not beeing checked. Used where the speed is important
and some corrupted data wont cause too much trouble ex streaming or
video games.
'''

import socket

def main():
    '''The main function.'''
    host = '127.0.0.1'
    port = 5000

    #as the TCP protocol is default socket socket.AF_INET, socket.SOCK_DGRAM
    #are used to change it to UDP
    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sck.bind((host, port))

    print("Server Started")
    while 1:
        data, addr = sck.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message From:", addr)
        print("Form connected user:", data)
        data = data.upper()
        print("Sending:", data)
        sck.sendto(data.encode('utf-8'), addr)
    sck.close()

if __name__ == '__main__':
    main()
