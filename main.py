from KeyboardInput import KeyboardInput
from FCFS import FCFS
inputer=KeyboardInput()
queue=inputer.wczytaj()
FCFS=FCFS(queue)
print("Sredni czas oczekiwania na algorytmu FCFS: " + str(FCFS.AVT))
print(FCFS.ProcessInfo)
print("Sredni czas oczekiwania na algorytmu SFJ: " + str(FCFS.AVT))
print("Sredni czas oczekiwania na algorytmu Round Robin: " + str(FCFS.AVT))