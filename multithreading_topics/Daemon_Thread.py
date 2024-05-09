"""
    When you open a IDLE app, 
    below thread runs: 
    1. Main thread
    2. Thread for interactive shell
    3. Thread for text highlighting
    4. Thread for memory management
    when you open editor another thread also runs
    5. Thread for editor - runs.
    when you run the code in editor interpreter thread runs.
    6. Thread for interpreter.
"""
# 2 types of Threads: 1. Daemon Thread (supportive) 2. Non Daemon Thread (non-supportive)
# above 1,2,5,6 are non-Daemon thread, while 3,4 are Daemon threads.

# Program will not terminate untill all nondaemon thread gets completed.
# Daemon Thread: It is thread which runs continueously in background and provide support to other nondaemon thread.
# Daemon threads are often used for tasks such as monitoring, background services or clean up operations.

# What decides thread is Daemon.
# t1 = threading.Thread(task=target)
# t1 = object which has instance variables.
# instance variables: name, ident, native id, daemon(True/False)
# print(t1.daemon) to check.

# How to change the daemon nature of thread.
# t1.daemon = True  -- before running thread. can't change daemon of running thread.

# checking daemon nature of main thread

import threading

obj = threading.currentThread()

print(obj.daemon)


def display():
    print('This is display function.')
    t2 = threading.Thread(target=demo)
    print(t2.daemon)                   # thread inherits the daemon nature from parent thread.

def demo():
    print('In thread 2')

t1 = threading.Thread(target=display)
print('Daemon nature of t1 is: ', t1.daemon)
t1.daemon =True                          # changing the daemon nature of thread.
print('Daemon nature of t1 is: ', t1.daemon)
t1.start()


# Example: use case. 

import threading,time

def display():
    for i in range(10):
        print(f'Teaching session.. {i}')
        time.sleep(0.5)
    
t1 = threading.Thread(target=display)
t1.daemon = True
t1.start()

time.sleep(3)
print('Exam time!')
print('Exam Over!')

# you can create n number of daemon threads.