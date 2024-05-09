# race condition: when 2 threads try to add and substract from a variable,
# it might give unexpected result.

# Below steps are performed while doing any operation.
# 1. Read the current value of a variable. x = 100
# 2. Calculate a new value for a variable. +10/-20
# 3. Write a new value for a variable. 110/80

#         t1               t2
# 1.      100              100
# 2.      110              80
# 3.      x = 110          x =80 (final)

# Bus Ticketing System

from threading import *

class Bus:
    def __init__(self,name,available_seats):
        self.available_seats = available_seats
        self.name = name
    def reserve(self,need_seats):
        print('Available seats are: ',self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}.")
            self.available_seats -=need_seats
        else:
            print('Sorry, seats are not available.')   
            
b1 = Bus('Mahaveer Travels',2)
t1 = Thread(target=b1.reserve,args=(1,),name='Chetan')
t2 = Thread(target=b1.reserve, args=(2,),name='Ram')
t1.start()
t2.start()


# Race condition: It is a bug generated by multiprocessing. 
# It occurs because 2 or more threads tries to update same variable and results into unreliable output.
# concurrent access to resources.

# To deal with this, use thread syncronization technique.
# A common approach is to protect the critical section of the code.(prevent concurrent access.)
# 1. using locks 2. using R-lock 3. using semaphores.


