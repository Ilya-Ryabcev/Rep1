















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