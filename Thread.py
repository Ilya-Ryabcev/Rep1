

















# import threading
# from time import sleep
#
#
# def slip(num:int, name:str):
#     print(f'{num}: {name}')
#     sleep(num)
#     print(f"После спячки {num}: {name}")
#
# t1 = threading.Thread(target=slip, args=(5, "Bob"))
# t2 = threading.Thread(target=slip, args=(3, "Masha"))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# import threading
#
# def hello():
#     print("Hello, world!")
#
# Создание таймера
# t = threading.Timer(5.0, hello)
# t.start()  # Запуск таймера
#
# Остановка таймера до выполнения
# t.cancel()
#
#
# import threading
#
# class New(threading.Thread):
#     def run(self):
#         print('1')
#
# t = New()
# t.start()
# t.join()
# print(t.is_alive())


# import threading
#
# def worker(num:int, text:str):
#     print(f'worker {num}: {text}')
#
# t = threading.Thread(target=worker, args=(1, "Hello"))
# t.start()
# t.join()