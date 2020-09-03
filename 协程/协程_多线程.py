import time
import threading
import asyncio
##################################################################
# await + 可等待的对象(协程对象、Future、Task对象、IO等待)
# 执行协程函数创建协程对象，函数内部代码不会执行，如果想要运行协程函数，必须要将协程对象交给事件循环来出来
# asyncio.run(foo()) 



##################################################################
# 主进程里开启主线程，主线程里开启2个线程，其中一个 线程里开启一个协程

async def foo():
    while True:
        print("xiecheng func...")
        await asyncio.sleep(1)


class Threads1(threading.Thread):
    def run(self): 
        while 1:
            print("in Threads1 ... ")
            time.sleep(1)


class Threads2(threading.Thread):
    def run(self): 
        # asyncio.run(foo()) 
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(foo())
        while 1:
            print("in Threads2 ... ")
            time.sleep(1)





def main(): 
    AICaculThread =Threads1()
    AICaculThread.setDaemon(True)
    AICaculThread.start()

    AICheckThread = Threads2()
    AICheckThread.setDaemon(True)
    AICheckThread.start()
    time.sleep(10)


main()



