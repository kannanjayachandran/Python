import threading
from time import sleep

class First_thread(threading.Thread):

    def run(self) -> None:
        for _ in range(10):
            print('Thread 1')
            sleep(0.1)
        return super().run()

class Second_thread(threading.Thread):

    def run(self) -> None:
        for _ in range(10):
            print('Thread 2')
            sleep(0.1)
        return super().run()

class third_thread(threading.Thread):

    def run(self) -> None:
        for _ in range(10):
            print('Thread 3')
            sleep(0.1)
        return super().run()

t1 = First_thread()
t2 = Second_thread()
t3 = third_thread()

t1.start()
sleep(0.3)
t2.start()
sleep(0.3)
t3.start()

# Here we are running two threads 
