# 1. timer object  2. barrier object

# 1. timer: 

import threading

def task():
    for i in range(5):
        print('Hello')
        
timer = threading.Timer(10,task)
timer.start()

for i in range(5):
    print('Main thread')
    
    
# 2. Barrier object: allows thread to wait for each other at specific point in their execution 
#    before proceeding further.

'''
Real life examples: 
1. cycle racing: race preparation, actual race, results
2. voting : voting in EVM, counting, result
3. Data: Data cleaning, Data Analysis on complete data, Final results.
'''

import threading,time

def player(name):
    print(f"{name} started.")
    score = 0
    for i in range(5):
        time.sleep(3)
        print(f"{name} is playing.")
        
    # barrier
    barrier.wait()
    
    # code for session end and distributing winning amount.
    print(f"{name} scored {score}")
    
    print(f"sending winning amount to {name}")
    
players = ['raj','sayali','jay','ayesha']

Threads = []

barrier = threading.Barrier(len(players))

for name in players:
    thread = threading.Thread(target=player,args=(name,))
    Threads.append(thread)
    thread.start()