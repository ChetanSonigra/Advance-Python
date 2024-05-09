# when exception occur in one thread, it will not impact other threads.
# when exception occurs in thread, it calls threading.exceptionhook function.
# interpreter calls threading.exceptionhook with 1 arg: named tuple with 4 values:
# 1. exception class 2. exception instance/value  3. a traceback object 4. thread
# main thread --> sys.exceptionhook
# created thread --> threading.exceptionhook --> sys.exceptionhook

import threading
import time

def customhook(args): 
    print('Exception occured in thread.')
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    
def display():
    for i in range(4):
        time.sleep(0.5)
        print('Hello'+10)
        
def show():
    for i in range(4):
        print('Hello')
        time.sleep(0.5)
        
threading.excepthook = customhook   # overriding exceptionhook function.
t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(4):
    print('Bye')


# Lifecycle of thread:
# A thread is a flow of execution in a program.
# every python program has atleast one thread of execution called main thread.
# Both processes and threads are created and managed by os.

    """
    new thread
    |
    running thread <--> blocked thread
    |
    terminated thread
    
    """
    