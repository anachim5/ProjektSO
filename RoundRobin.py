class RoundRobin(object):
    def __init__(self,queue):
        self.queue=queue
    def RunQ(self):
        time=0
        q=[]
        while(True):
            for process in self.queue:
                if(process[2]<=time):
                    q.append(process)
            Quantum=2
            
            if not q:
                break
