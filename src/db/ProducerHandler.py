from threading import Thread, Condition

import threading, time, re, socket, binascii, random

data1 = "313131303320203230313430313238313133323339393036323733204755534552494e464f322020"
data2 = "202020202020202020475a3030304b46202020205a3030304b45465520202020202020202020202031202020203120202020201a"

MAX_NUM = 1000
condition = Condition()


# Producer thread
class Producer(Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self, name="Producer")
        self.data = queue

    def run(self):
        num = 20000000
        while True:
            for x in [130, 131, 132, 155, 156, 133, 186, 145]:
                phonenum = str(x) + str(num).zfill(8)
                if not self.search(phonenum):
                    condition.acquire()
                    if len(queue) == MAX_NUM:
                        condition.wait()
                    self.data.append(phonenum)
                    condition.notify()
                    condition.release()

            if num >= 29999999:
                break
            num += 1

    def search(self, strs):
        if re.search(r'(\d)\1{4,}', strs):
            return True
        else:
            return False


#Handler Thread
class Handler(threading.Thread):
    def __init__(self, name, queue, h_file, mutex):
        threading.Thread.__init__(self, name=name)
        self.data = queue
        self.__file = h_file
        self.__mutex = mutex

    def run(self):
        while True:
            try:
                condition.acquire()
                if not self.data:
                    condition.wait()
                phonenum = self.data.pop()
                condition.notify()
                condition.release()

                address = ("132.42.33.130", 8002)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                data = binascii.a2b_hex(data1) + phonenum + binascii.a2b_hex(data2)
                s.connect(address)
                s.send(data)
                time.sleep(random.randint(1, 4));
                recvdata = s.recv(4096 * 2)
                s.close()
                #print recvdata.decode('gbk')
                if recvdata and recvdata.startswith("111012"):
                    while mutex:
                        self.__file.write("recvdata")
            except IOError:
                print "IOError"


if __name__ == "__main__":
    queue = []
    Producer(queue).start()
    time.sleep(2)
    mutex = threading.Lock()
    result_file = open("./db2.txt", "a", 1)
    for i in xrange(50):
        Handler("Thread" + str(i), queue, result_file, mutex).start()
