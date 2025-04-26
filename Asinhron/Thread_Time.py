

import asyncio

async def greet():
    print('1')
    await asyncio.sleep(3)
    print('2')

loop = asyncio.get_event_loop()
loop.run_until_complete(greet())
loop.close()













# import threading


# def work(num:int):
#     print(f'Работает под номером {num}')
#
# t = threading.Timer(3.0, work, args=[3])
# t.start()
# t.join()



# import threading
#
# def greet(num:int, name:str):
#     print(f'номер {num} зовут {name}')
#
# t1 = threading.Thread(target=greet, args=(5, "Bob"))
# t2 = threading.Thread(target=greet, args=(3, "Alise"))
# t1.start()
# t2.start()
# t1.join()
# t2.join()