# Algorytm wybiera proces ktry dotarl najwczesniej i wykonuje go do konca
import time
class FCFS():
    def __init__(self):
        self.queue=[]
    def AddProcess(self,Time,arrivalTime):
        self.queue.append([Time,arrivalTime])
    def RunQ(self):
        self.queue.sort(self,key=lambda tup:tup[1])
        for i in self.queue:
            time.sleep(i[0])
