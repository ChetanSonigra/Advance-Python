# Syncronization Technique:
#     Thread syncronization is defined as a mechanism which ensures that
#     2 or more concurrent threads do not simultaneously execute some particular program segment
#     known as critical section.

# 3 techniques: 1. Locks 2. R-Locks 3. Semaphores
# 1. Lock:

from threading import *
import time

mylock = Lock()

def task(mylock,msg):
    mylock.acquire()   # optional default arguments blocking=True, timeout =-1
    for i in range(5):
        print(msg)
    time.sleep(3)
    mylock.release()
    
t1 = Thread(target=task,args=(mylock,'Hello World',))
t2 = Thread(target=task, args=(mylock,'Hellow...'))

t1.start()
t2.start()
t1.join()
t2.join()

class Bus:
    def __init__(self,name,available_seats,l):
        self.available_seats = available_seats
        self.name = name
        self.l= l
    def reserve(self,need_seats):
        self.l.acquire()
        print('Available seats are: ',self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}.")
            self.available_seats -=need_seats
        else:
            print('Sorry, seats are not available.') 
        self.l.release()  
            
b1 = Bus('Mahaveer Travels',2,mylock)
t1 = Thread(target=b1.reserve,args=(2,),name='Chetan')
t2 = Thread(target=b1.reserve, args=(0,),name='Ram')
t1.start()
t2.start()

# can't acquire/release lock once it is already acquired/released.

# 2. R-Lock:
# By using R-Lock, you can acquire lock multiple times. 
# Useful when functions already uses locks and agian it is used in other program.
# R-Lock is just modified version of Lock.

mylock = RLock()

class Bus:
    def __init__(self,name,available_seats,l):
        self.available_seats = available_seats
        self.name = name
        self.l= l
    def reserve(self,need_seats):
        self.l.acquire()
        self.l.acquire()
        print(self.l)            # rlock gives thread information.
        print('Available seats are: ',self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}.")
            self.available_seats -=need_seats
        else:
            print('Sorry, seats are not available.') 
        self.l.release()  
        self.l.release()
            
b1 = Bus('Mahaveer Travels',2,mylock)
t1 = Thread(target=b1.reserve,args=(2,),name='Chetan')
t2 = Thread(target=b1.reserve, args=(0,),name='Ram')
t1.start()
t2.start()

# 3. Semaphore

# To execute a particular number of threads at a time. 
# in lock/rlock only one thread works at a time.
# Semaphore can be used to limit the access to the shared resources with limited capacity.


obj = Semaphore(2)

def display(name):
    # calling acquire method.
    # acquire - decrement count.
    obj.acquire()
    for i in range(5):
        print('hellow')
        print(name)
        time.sleep(0.5)
    # calling release method
    # release - increment count
    obj.release()    
    # obj.release() 
    # by mistake if we add additional release without acquire, it will cause issue in counter.
    # to address this, use BoundedSemaphore()
        
t1 = Thread(target=display,args=('Thread 1',))
t2 = Thread(target=display,args=('Thread 2',))
t3 = Thread(target=display,args=('Thread 3',))
t4 = Thread(target=display,args=('Thread 4',))
t5 = Thread(target=display,args=('Thread 5',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

