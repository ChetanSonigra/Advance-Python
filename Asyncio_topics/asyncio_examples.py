import asyncio,aiohttp,time,aiofiles,smtplib

# Example 1: getting movie tickets and liking instagram pictures.
def get_movie_tickets():
    print('waiting in line')
    time.sleep(7)
    print('Got the movie tkt')
    
def like_insta_pictures():
    time.sleep(3)
    print('Finished Liking Pictures.')

def main():
    get_movie_tickets()
    like_insta_pictures()
    
start= time.time()
main()
print('Syncronous time: ', time.time()-start)

async def get_movie_tickets():
    print('waiting in line')
    await asyncio.sleep(7)
    print('Got the movie tkt')
    
async def like_insta_pictures():
    await asyncio.sleep(3)
    print('Finished Liking Pictures.')

async def main():               # same as syncronous time
    await get_movie_tickets()
    await like_insta_pictures()
    
async def main():                           # This is done asyncronously.
    task1 = asyncio.create_task(get_movie_tickets())
    # await like_insta_pictures()
    # await task1
    task2 = asyncio.create_task(like_insta_pictures())
    await task1,task2


start= time.time()
asyncio.run(main())
print('Asyncronous time: ', time.time()-start)


# Example 2: File IO
# Use aiofiles - to handle files with async.
# Use aiohttp - to get files with http request with async.
def fetch_files():
    print('Starting to fetch a file.')
    time.sleep(1)                  
    print('Fetching file completed.')
    
def main():
    print('Starting Main')
    fetch_files()
    fetch_files()
    fetch_files()
    print('Main completed')
    
start = time.time()
main()
print('Syncronous program took: ',time.time()-start, 'sec')



async def fetch_files():
    print('Starting to fetch a file.')
    await asyncio.sleep(1)                  
    print('Fetching file completed.')
    
async def main():
    print('Starting Main')
    await asyncio.gather(     # executes all coroutines concurrently. You don't have to create tasks.
    fetch_files(),
    fetch_files(),
    fetch_files()
    )
    print('Main completed')
    
start = time.time()
asyncio.run(main())
print('Asyncronous program took: ',time.time()-start, 'sec')

# # Example 3: Sending emails - sendgrid,twilio,smtplib

# async def send_mail(subject,body,to):
#     connection = smtplib.SMTP('smtp.gmail.com')
#     connection.ehlo()
#     connection.starttls()
#     sender_mail = 'abc@gmail.com'
#     receipient_mail = 'abc@gmail.com'
#     connection.login(sender_mail,'****')
#     header = 'To: ' +receipient_mail+'\n'+'From:' \
#         +sender_mail+ '\n' + 'subject: test mail\n'
#     content = header + content
#     connection.sendmail(sender_mail,receipient_mail,content)
#     connection.close()
# async def main():
#     for i in range(50): 
#         asyncio.create_task(send_mail('Test Mail','This is a test mail.','abc@gmail.com'))
    
#     for i in range(50):
#         print(f'Doing other task while sending email: {i} - {i**5}')
#         time.sleep(0.2)
        
# start = time.time()
# asyncio.run(main())
# print(time.time()-start)

# Example 4: making http requests

import requests,time

pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

start = time.time()
for i in range(1,150):
    url_p = f'{pokemon_endpoint}{i}'
    print(pokemon_endpoint)
    response = requests.get(url_p)
    print(response)
    if response.status_code==200:
        pok = response.json()
        print(pok['name'])
print('Syncronous program took: ',time.time()-start, 'sec')  #179 sec


async def main():
    async with aiohttp.ClientSession() as session: 
        for i in range(1,150):
            url_p = f'{pokemon_endpoint}{i}'
            #print(pokemon_endpoint)
            async with session.get(url_p) as response:
            #print(response)
                pok = await response.json()
                print(pok['name'])
                
start = time.time()
asyncio.run(main())
print('Asyncronous program took: ',time.time()-start, 'sec') #9.83 sec
    




