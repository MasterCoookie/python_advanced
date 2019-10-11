'''
threading allows to use multiple thereadhs so the programme can
still responde while performing some task in the background. It is
extrimely useful while trying to write a program that has at least two different features.
Of course it wont work with the code where program logic runs in a sequence
'''
import time
from threading import Thread

def timer(name, delay, repeat):
    '''prints out current time every delay.'''
    print("Timer:", name, "started")
    while repeat > 0:
        time.sleep(delay)
        print(name, ":", time.ctime(time.time()))
        repeat -= 1
    print("Timer:", name, "completed")

def main():
    '''Main function.'''
    thread_1 = Thread(target=timer, args=("Timer1", 1, 5))
    thread_2 = Thread(target=timer, args=("Timer2", 2, 5))

    thread_1.start()
    thread_2.start()

    print("Main Completed")

if __name__ == '__main__':
    main()
