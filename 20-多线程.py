# import threading
# from threading import Thread
#
# def sum():
#     for i in range(10):
#         print(i, threading.current_thread().name)
#
# t=Thread(target = sum)
# #启动线程
# t.start()



import threading

class Mythread(threading.Thread):
    def run(self):
        self.show()

    def show(self):
        for i in range(10):
            print(self.name, i)

t = Mythread(name="多线程1")
t.start()#启动线程，线程启动后会自动执行run方法
t.join()#将t线程填加到主线程中，主线程等待t线程执行完毕后再执行，会阻塞主线程

