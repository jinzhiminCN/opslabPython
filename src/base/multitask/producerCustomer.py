#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import multiprocessing
from time import ctime
 
#设置哨兵问题
def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        #处理项
        item = input_q.get()
        if item is None:
            break
        #此处替换为有用的工作
        print("pull",item,'oout of q')
        #发出信号通知任务完成
       # input_q.task_done()
        #此句未执行，因为q.join()收集到四个task_done()信号后，主进程启动，未等到print此句
    print("Out of consumer:",ctime())
 
def producer(sequence,output_q):
    for item in sequence:
        print("Into procuder:", ctime())
        output_q.put(item)
        print("put",item,"into q")
    print("Out of procuder:",ctime())
 
if __name__ == '__main__':
    #做完了通知发个消息~
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p1 = multiprocessing.Process(target=consumer,args=(q,))
   # cons_p.daemon = True
    cons_p1.start()
 
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()
 
    #生产多个项，sequence代表要发送给消费者的项xulie
    #在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
 
    q.put(None)
    q.put(None)
 
    #等待所有项被处理
    cons_p1.join()
    cons_p2.join()

