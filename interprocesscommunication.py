import multiprocessing, time
# value, array, queue for interprocess communication.

def calc_squares(numbers,result,v,q):
    v.value=5.67
    for idx,i in enumerate(numbers):
        result[idx]=i**2
        q.put(i**2)


if __name__=='__main__':
    result = multiprocessing.Array('i',8)
    numbers = [i for i in range(8)]
    v = multiprocessing.Value('d',0.0)
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=calc_squares,args=(numbers,result,v,q))
        
    p1.start()
    
    p1.join()
    
    print(result[:],len(result),v.value,q)
    while not q.empty():
        print(q.get())
        
# processing lock

def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value+1
        lock.release()
    
def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value-1
        lock.release()
        
if __name__=='__main__':
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit,args=(balance,lock))
    p2 = multiprocessing.Process(target=withdraw,args=(balance,lock))   
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print(balance.value)
