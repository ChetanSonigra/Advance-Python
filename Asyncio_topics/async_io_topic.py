import asyncio
import time
# syncronous programming is program that runs sequencially.
# so, speed depends on speed of processor.
# regular python code runs on one process and one thread.
# asyncrony refers to occurance of events independent of main program flow and way to deal with such events.
# coroutines are computer program component that generalize subroutines for non-preemptive multitasking by allowing execution to be suspended and resumed.
# event-loop is a programming construct or design pattern that waits for and dispatches events/msgs in program.
# asyncio.run() creates eventloop, runs and monitor coroutines.
# Multithreading is about workers while asyncronous programming is about tasks.

async def main():   # creates a coroutine object.

    print('Hellow')
    task = asyncio.create_task(foo('sldfj')) # creating task will run asap when another program is not running.
    # await task      # this will stop further execution untill task is finished.
    await asyncio.sleep(6) # this will allow task to run before 'finished.'
    print('Finished.')

async def foo(text):
    print(text)
    await asyncio.sleep(5)

print(main()) # coroutine object

start = time.time()
asyncio.run(main()) # creates event-loop to execute coroutines. # coroutine provided is entry point for program.
end = time.time()
print(f'Took {end-start} seconds.')


async def fetch_data():        # when coroutines returns something, it's called future.
    print('Start fetching...')
    await asyncio.sleep(2)
    print('Done fetching...')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    
    value = await task1    # without await it will not wait.
    print(value)
    await task2          # without this main will finish without executing task2
   
    
start = time.time()
asyncio.run(main()) # creates event-loop # coroutine provided is entry point for program.
end = time.time()
print(f'Took {end-start} seconds.')


async def main():
    task1 = asyncio.create_task(fetch_data())
    value = await task1
    task2 = asyncio.create_task(print_numbers())
    task3 = asyncio.create_task(fetch_data())
    await task2
    await task3

start = time.time()
asyncio.run(main()) # creates event-loop # coroutine provided is entry point for program.
end = time.time()
print(f'Took {end-start} seconds.')

# custom event loop: 
loop = asyncio.new_event_loop()

task1 = asyncio.sleep(2)  # creates a coroutine

loop.run_until_complete(task1)

print('Done')

# async - tells that this function is allowed to run concurrently.
# await - makes function to run in order.

def http_get_sync(url: str) -> dict:
    s = requests.get(url)
    return s.json()

async def http_get(url: str) -> dict:
    return await asyncio.to_thread(http_get_sync,url)

# or 
async def http_get(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
        

import asyncio,random,requests,time,aiohttp

MAX_POKEMON = 800

def get_random_pokemon_name_sync():
    pk_id = random.randint(1,MAX_POKEMON)
    pk_url = f'https://pokeapi.co/api/v2/pokemon/{pk_id}'
    pokemon = http_get_sync(pk_url)
    return str(pokemon['name'])

async def get_random_pokemon_name():
    pk_id = random.randint(1,MAX_POKEMON)
    pk_url = f'https://pokeapi.co/api/v2/pokemon/{pk_id}'
    pokemon = await http_get(pk_url)
    return str(pokemon['name'])

async def main():
    start = time.perf_counter()
    for i in range(250):
        pk_name = await get_random_pokemon_name()
        print(pk_name)
    print('Total time syncronous: ', time.perf_counter()-start)
    
    start = time.perf_counter()
    # result = await asyncio.gather(*[get_random_pokemon_name() for i in range(250)])
    # gather or create task, await or TaskGroup
    async with asyncio.TaskGroup() as tg:
        tasks =[]
        for i in range(250):
            task = tg.create_task(get_random_pokemon_name())
            task.append(task)
    result = [task.result() for task in tasks]
    
    print(result)
    print('Total time asyncronous: ', time.perf_counter()-start)
    
asyncio.run(main())
    
    
lock = asyncio.Lock()
semaphore = asyncio.Semaphore(2)
event = asyncio.Event()  # use event.wait() , event.set() to handle code execution.
shared_resource = 0
async def modify_shared_resource():
    async with lock:
        global shared_resource
        shared_resource += 1
        await asyncio.sleep(1)
    
async def main():
    await asyncio.gather(*[modify_shared_resource() for i in range(20)])
    
asyncio.run(main())
print(shared_resource)


