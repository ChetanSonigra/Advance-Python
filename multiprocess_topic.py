import multiprocessing
print(multiprocessing.cpu_count())
import time


def calc_squares(numbers):
    print('calculate square of numbers')
    for n in numbers:
        print(n**2)
        
def calc_qubes(numbers):
    global result
    print('calculate square of numbers')
    for n in numbers:
        result.append(n**3)
    print('inside process: ', result)
    
    
def calc_quardrant(numbers):
    global result
    print('calculate quadrant of numbers.')
    for n in numbers:
        print(n**4)
        result.append(n**4)


if __name__=='__main__':
    array=[i for i in range(2000)]
    result = []     # copies data in separate processes.
    start = time.time()
    #p1 = multiprocessing.Process(target=calc_squares,args=(array,))
    p2 = multiprocessing.Process(target=calc_qubes,args=(array,))
    p3 = multiprocessing.Process(target=calc_quardrant,args=(array,))
    
    #p1.start()
    p2.start()
    p3.start()

    #p1.join()
    p2.join()
    p3.join()

    print(time.time()-start)
    print('outside process:' ,result)   
    # new process copies data from main program in its own address space.
    # to deal with this is to use shared memory which is outside processes.

