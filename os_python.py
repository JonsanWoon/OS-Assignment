import threading
import time
import random
import signal

exitFlag = 0


class  semaphore():
    semDetect = 0
    semDrill = 0
    semClean = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    

class detect(myThread):
    def run(self):
        print("Starting " + self.name)
        while not exitFlag:
            if semaphore.semDetect==1:
                working(self.name, 3)
                randommm = random.randint(0,1)
                if randommm ==1:
                    semaphore.semDrill = 1
                    semaphore.semDetect =0
                    print("Exiting " + self.name + " System")   
                    print("Activate Drill System")
                    print(" ")
            # time.sleep(10)
        

class drill(myThread):
    def run(self):
        print("Starting " + self.name)
        while not exitFlag:
            if semaphore.semDrill==1:
                # threadLock.acquire()
                working(self.name, 1)
                # threadLock.release()
                semaphore.semDrill = 0
                semaphore.semDetect = 1
                semaphore.semClean =1
                print("Exiting " + self.name + " System")
                print("Activate Detect System")
                print("Activate Clean System")
                print(" ")
            time.sleep(10)

class clean(myThread):
    def run(self):
        print("Starting " + self.name)
        while not exitFlag:
            if semaphore.semClean==1:
                working(self.name, 10)
                semaphore.semClean=0
                print("Exiting " + self.name + " System")
                print(" ")
            time.sleep(10)
            

def working(threadName, counter):
    while counter>0:
        print("%s running: %s..." % (threadName, counter))
        counter -= 1
    return


def main():
    semaphore.semDetect = 1
    # threadLock = threading.Lock()
    # Create new threads
    thread1 = detect("Detect")
    thread2 = drill("Drill")
    thread3 = clean("Clean")
    # Start new Threads

    thread1.start()
    thread2.start()
    thread3.start()

    print("Exiting main Thread")


if __name__ == '__main__':
    main()




