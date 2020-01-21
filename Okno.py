from tkinter import *
class Okno(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Wyjdz"
        self.QUIT["fg"]   = "blue"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "right"})





root = Tk()
app = Okno(master=root)
app.mainloop()
root.destroy()