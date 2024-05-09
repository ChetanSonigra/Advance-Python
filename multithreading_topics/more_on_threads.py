# Built-in functions:
# is_alive(): checks thread is running or not.
# active_count(): number of running threads.
# enumerate(): list of all running threads.
# main_thread(): returns the main thread details.
# get_native_id(): gives native id of thread.

from threading import Thread,main_thread,active_count,enumerate,get_native_id

def display():
    print(main_thread())
    print(get_native_id())
    for i in range(5):
        print('Hello World. this is in t1.')
    
def show():
    for i in range(5):
        print('Hi, This is in t2.')
        

t1 = Thread(target=display)
print(t1.is_alive())
t1.start()
print('Running threads: ',enumerate())
print('Number of threads: ',active_count())  

print(get_native_id())
print(t1.is_alive())    
for i in range(5):
    print()

# Join method: when a thread wants to wait for another thred to complete. Use this method.

from threading import Thread,main_thread,active_count,enumerate,get_native_id

def display():
    print(main_thread())
    print(get_native_id())
    for i in range(5):
        print('Hello World. this is in t1.')
    
def show():
    for i in range(5):
        print('Hi, This is in t2.')
        
t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
#t1.join()            # ensures t1 is completed at this point. t2 and main runs parallelly then.
t2.start()
t2.join()
for i in range(5):
    print('This is in main thread.')
    