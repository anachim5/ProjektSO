# Algorytm wybiera proces ktory dotarl najwczesniej i wykonuje go do konca
class FCFS(object):
    def __init__(self,queue):
        self.queue=queue
        self.AVT=0
        self.ProcessInfo=[]
        self.RunQ()
    def RunQ(self):
        for i in self.queue:
            if(i==self.queue[-1]):
                continue
            self.AVT+=int(i[2])
            self.ProcessInfo.append((i[0],"Czas oczekiwania: " +str(self.AVT)))
        self.AVT=self.AVT/len(self.queue)

            