class SFJ(object):
    def __init__(self,queue):
        self.queue=queue
        self.AVT=0
        self.RunQ()
    def RunQ(self):
        time=0
        
        while(True):
            q=[]
            for process in self.queue:
                if(int(process[2])<=time):
                    q.append(process)
            if not q:
                break
            print("Czas: "+str(time))
            print("Kolejka:")
            print(q)
            q.sort(key=lambda tup: tup[1])
            print("Wykonywany proces: "+q[0][0]+"\n")
            time+=int(q[0][1])
            self.queue.remove(q[0])
            