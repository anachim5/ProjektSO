from tkinter import *

class Okno(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def FromFile(self):
        print ("Algorytm FCFS")
        pass
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Wyjdz"
        self.QUIT["fg"]   = "blue"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        self.fcfs = Button(self)
        self.fcfs["text"] = "Z pliku"
        self.fcfs["command"] = self.FromFile()
        self.fcfs.pack({"side": "left"})

        self.fcfs2 = Button(self)
        self.fcfs2["text"] = "Z klawiatury"
        self.fcfs2["command"] = self.FromFile()
        self.fcfs2.pack({"side": "left"})


root = Tk()
app = Okno(master=root)
app.mainloop()
root.destroy()