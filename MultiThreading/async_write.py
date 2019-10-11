'''
this basic program writes a file in a background using multithreading.
The join() function waits until other threads finish their tasks.
'''

import threading
import time

class AsyncWrite(threading.Thread):
    '''writes a file in the bcg'''
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        file = open(self.out, 'a')
        file.write(self.text+'\n')
        file.close()
        time.sleep(2)
        print("File writing finished to", self.out)

def main():
    '''the main fun'''
    msg = input("Enter a string to store: ")
    background = AsyncWrite(msg, 'out.txt')
    background.start()
    print("The program can continue while it writes in another thread")
    print('12 + 48 =', 12 + 48)

    background.join()
    print("Waited until thread was complete")

if __name__ == '__main__':
    main()
