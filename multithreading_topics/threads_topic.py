import threading,os
import time

print(os.getpid())    # process id
# Threads are python objects of threading.Thread class.
print(threading.current_thread())
print(threading.current_thread().name, threading.current_thread().ident)
print(threading.current_thread().is_alive())

# 2 ways to create threads.
# 1. using thread class 2. by extending thread class.
# class Myclass(Thread):
#     def run(self):
#         for vid in videos:
#            print(f'{vid} uploading...')
#            time.sleep(3)
#            print(f'{vid} uploaded.')
# can overwrite init method to provide new variables.
# can call variables in run/init method with t1.var_name outside class.

# creating threads for method. 
# class/static method --> target=class_name.method_name 
# instance method --> target=object_name.method_name

def calc_squares(numbers):
    print('calculate square of numbers')
    for n in numbers:
        print(n**2)
        
def calc_qubes(numbers):
    print('calculate cube of numbers')
    print('t2 thread: ', threading.current_thread())
    for n in numbers:
        print(n**3)
        
def calc_quadrant(numbers):
    print('calculate quadrant of numbers')
    print('t3 thread: ', threading.current_thread())
    for n in numbers:
        print(n**4)

array=[i for i in range(2)]
start = time.time()
#t1 = threading.Thread(target=calc_squares,args=(array,))
t2 = threading.Thread(target=calc_qubes,args=(array,))
t3 = threading.Thread(target=calc_quadrant,args=(array,))

# print thread names,ids. ids are read-only.
print(t2.name,t3.name)
print(t2.getName()) # Deprecated.
print(t2.ident,t2.native_id)     # native_Id assigned by os, ident assigned by interpreater.

# change the thread name
t2.name = 'Ram'
threading.current_thread().name = 'Chetan'
print(t2.name,threading.current_thread().name)

#t1.start()
t2.start()
t3.start()

#t1.join()
t2.join()
t3.join()

print(time.time()-start)

