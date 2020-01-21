class KeyboardInput(object):
    def __init__(self):
        pass
    def wczytaj(self):
        queue=[]
        i=input("Wczytaj ilosc  procesów: ")
        for procesy in range(0,int(i)):
            queue.append(("Proces#"+str(procesy+1),input("Czas dzialania # "+str(procesy)+": "),input("Czas dotarcia # "+str(procesy)+": ")))
        queue=sorted(queue, key=lambda tup: tup[1])
        #print(queue)
        return queue