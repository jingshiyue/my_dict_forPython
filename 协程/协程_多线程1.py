import time
import threading
import asyncio
##################################################################
# 教程: https://www.cnblogs.com/ssyfj/p/9219360.html
# await + 可等待的对象(协程对象、Future、Task对象、IO等待)
# 协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他协程也挂起，或者执行完毕
# 使用asyncio.sleep模拟阻塞操作
# tasks = asyncio.gather(*[task1,task2])　　　　#gather可以实现同时注册多个任务，实现并发操作。wait方法使用一致
# 执行协程函数创建协程对象，函数内部代码不会执行，如果想要运行协程函数，必须要将协程对象交给事件循环来出来
# asyncio.run(foo()) 

# coroutine1 = func1(5)
# coroutine2 = func1(3)
# loop = asyncio.get_event_loop()
# task1=asyncio.ensure_future(coroutine1)  #创建任务，coroutine1是协程对象，把协程对象转换成任务
# task2=asyncio.ensure_future(coroutine2)
# tasks = asyncio.gather(*[task1,task2])　　　　#gather可以实现同时注册多个任务，实现并发操作。wait方法使用一致
# loop.run_until_complete(tasks)
# loop.close()   #事件循环关闭

# task1=asyncio.ensure_future(coroutine1)
# task2=asyncio.ensure_future(coroutine2)
# tasks = asyncio.wait([task1,task2])  #wait跟gather一样 实现并发
# loop.run_until_complete(tasks)

# asyncio.Task.all_tasks()   查看循环事件里
"""
协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象.
run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，task是Future的子类,保存了协程运行后的状态，用于未来获取协程的结果
"""

##################################################################
# 主进程里开启主线程，主线程里开启2个线程，其中一个 线程里开启一个协程

#设为异步函数
# @asyncio.coroutine
# def func1(num):
#     print(num,f'before---func{num}----')
#     yield from asyncio.sleep(5)
#     print(num,f'after---func{num}----')

# task = [func1(1),func1(2)]

# if __name__ == "__main__":
#     begin = time.time()
#     loop = asyncio.get_event_loop()  #进入事件循环
#     loop.run_until_complete(asyncio.gather(*task))  #将协同程序注册到事件循环中
#     loop.close()
#     end = time.time()
#     print(end-begin)
##################################################################

##################################################################
# import asyncio,time

# async def func1(num): #使用async关键字定义一个协程，协程也是一种对象，不能直接运行，需要加入事件循环中，才能被调用。
#     print(num,'before---func1----')

# if __name__ == "__main__":
#     begin = time.time()

#     coroutine = func1(2)
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(coroutine)
#     loop.close()
#     end = time.time()
#     print(end-begin)
##################################################################
##################################################################
#  协程嵌套，将多个协程封装到一个主协程中
# import asyncio,time

# async def func1(num):
#     print(num,'before---func1----')
#     await asyncio.sleep(num)
#     return "recv num %s"%num

# async def main():
#     coroutine1 = func1(5)
#     coroutine2 = func1(3)
#     coroutine3 = func1(4)

#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3),
#     ]

#     dones, pendings = await asyncio.wait(tasks)  #也可以用gather获取结果 results = await asyncio.gather(*tasks)

#     for task in dones: #对已完成的任务集合进行操作
#         print("Task ret: ",task.result())

# if __name__ == "__main__":
#     begin = time.time()

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()
#     end = time.time()
#     print(end-begin)
##################################################################
##################################################################
    #    任务取消
# import asyncio,time

# async def func1(num):
#     print(num,'before---func1----')
#     await asyncio.sleep(num)
#     return "recv num %s"%num

# if __name__ == "__main__":
#     begin = time.time()

#     coroutine1 = func1(5)
#     coroutine2 = func1(3)
#     coroutine3 = func1(4)

#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3),
#     ]


#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         print(asyncio.Task.all_tasks())
#         for task in asyncio.Task.all_tasks():#获取所有任务
#             print(task.cancel())#单个任务取消
#         loop.stop()#需要先stop循环
#         loop.run_forever()#需要在开启事件循环
#     finally:
#         loop.close()#统一关闭
#     end = time.time()
#     print(end-begin)
##################################################################
