# In con-current programming, sometimes we need to co-ordinate threads.
# Threads communicate each-other via signals.
# 3 ways: 1. By creating event object 2. By creating condition object  3. By using queue model.

# 1. Event module: 
# methods of Event class: 
# 1) set(): set the interanl flag to True. if flag is True, waiting thread is awakened.
# 2) reset(): reset the internal flag to False, other thread will wait again.
# 3) is_set(): return boolean of whether flag is True/False.
# 4) wait([timeout]): calling this function keep the other thread on wait until flag is True. Default timeout is -1.
import threading
import time

# Example 01:

e = threading.Event()

def task():
    print('Game is started.')
    time.sleep(3)
    e.set()
    
def end():
    e.wait()
    if e.is_set():
        print('Code for destroying session.')
          
def another_task():
    for i in range(5):
        print('another task')
        time.sleep(0.2)
        
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)
t3 = threading.Thread(target=another_task)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# Example 02:

e = threading.Event()
def light_switch():
    i =1
    while i<3:
        print('Light is green.')
        e.set()
        time.sleep(5)
        print('Light is red.')
        e.clear()
        time.sleep(5)
        i+=1
        e.set()
        

def traffic_message():
    e.wait()
    i = 1
    while e.is_set() and i<3:
        print('You can go.')
        time.sleep(0.5)
        i +=1
        if i<3:
            e.wait()
    
t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()

t1.join()
t2.join()

# Example 03: read large file 5 lines each time from one thread and write it to other file in thread 2.

e = threading.Event()
data = []
with open(r'C:\Users\sonigra.mansukhbhai\PycharmProjects\AdvancePython\Advance-Python\multithreading_topics\threads_details.txt','r') as f:
    f.read()
    end = f.tell()

def read_files():
    
    f = open(r'C:\Users\sonigra.mansukhbhai\PycharmProjects\AdvancePython\Advance-Python\multithreading_topics\threads_details.txt','r')
    while f.tell()!=end:
        global data
        for i in range(5):
            data.append(f.readline())
        while '' in data:
            data.remove('')
        print(data)
        # if len(data)==0:
        #     f.close()
        #     break
        e.set()
        time.sleep(5)
        data = []
    f.close()
    
def write_files():
    e.wait()
    while e.is_set():
        global data
        g = open(r'C:\Users\sonigra.mansukhbhai\PycharmProjects\AdvancePython\Advance-Python\multithreading_topics\threads_details2.txt','+a')
        for x in data:
            print(x)
            g.write(x)
        e.clear()
        if len(data)==5:
            e.wait()    
    g.close()
t1 = threading.Thread(target=read_files)
t2 = threading.Thread(target=write_files)

t1.start()
t2.start()

t1.join()
t2.join()


# 2. Condition Object:
# To communicate with multiple threads.
# con = threading.Condition([lock object])
# acquire: used to acquire the lock
# release: used to release the lock.
# wait: timeout=0 default. used to block the thread.
# notify(): wake up one thread.
# notify_all(): wake up multiple threads.

import threading,time

def write_data():
    con.acquire()
    with open('multithreading_topics/report.txt','w') as f:
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        for day in days:
            temp = input(f"Enter the temperature for the {day}")
            f.write(temp+"\n")
    con.notify_all()
    con.release()
    
def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('multithreading_topics/report.txt','r') as f:
        data = f.readlines()
        max1 = float(data[0].strip('\n'))
        for temp in data[1:]:
            temp = float(temp.strip('\n'))
            if temp>max1:
                max1 = temp
    print('Maximum temperature is: ',max1)
    con.release()
    
def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('multithreading_topics/report.txt','r') as f:
        data = f.readlines()
        sum1 = 0
        for temp in data:
            sum1 += float(temp.strip('\n'))
        average = round(sum1/len(data),2)
        print(f'Average temprature of week is {average}')
    con.release()


con = threading.Condition()
t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.run()
t2.run()
t3.run()



# 3. Queue Object:                            
# queue.Queue([maxsize]) - FIFO method.
# put(item,block=True) = insert item
# get() = get and delete the item
# Thread safe - no race condition
# implements all the required locking semantics.

import time,threading
import queue

def producer(my_que):
    print('Producer: running..')
    n = int(input('Enter number of students: '))
    for i in range(n):
        marks = float(input('Enter marks: '))
        my_que.put(marks)
    my_que.put(None)
    
    print('Producer: end')
def consumer(my_que):
    print('Consumer: running..')
    while True:
        item = my_que.get()
        if item is None:
            break
        print('Got ', item)
    print('Consumer: end')
    
my_que = queue.Queue()

t1 = threading.Thread(target=producer,args=(my_que,))
t2 = threading.Thread(target=consumer,args=(my_que,))

t1.run()
t2.run()