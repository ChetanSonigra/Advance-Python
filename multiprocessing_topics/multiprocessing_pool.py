import multiprocessing,time

def sum_squares(n):
    sum= 0
    for i in range(n):
        sum += i**2
    return sum
        

if __name__=='__main__':
    t1=time.time()
    p = multiprocessing.Pool()            # by default, it will create processes as many as logical cores of cpu
    result = p.map(sum_squares,range(30000))
    p.close()
    p.join()
    print('Pool took: ', time.time()-t1)
    
    t2 = time.time()
    
    result = []
    for i in range(30000):
        result.append(sum_squares(i))
        
    print('Serial processing took: ', time.time()-t2)
    
    t3 = time.time()
    
    with multiprocessing.Pool(4) as p:
        result =p.map(sum_squares,range(30000))
    print('with pool(4) took: ', time.time()-t3)