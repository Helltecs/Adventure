import tkinter
from tkinter import ttk
import pickle
import time

class MainGUI:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.window.geometry("900x450")
        self.window.title("Text RPG")
        self.mainframe = ttk.Frame(self.window, padding=10)
        self.mainframe.grid(column=0, row=0, sticky="wnse")
        self.frame = ttk.Frame(self.mainframe, borderwidth=5, relief="sunken", padding=5)
        self.frame.grid(column=1, row=0, sticky="nwe", pady=(0, 5), columnspan=2)
        self.frameInv = ttk.Frame(self.mainframe, relief="groove", padding=5)
        self.frameInv.grid(column=0, row=0, sticky="n")

        self.display = tkinter.StringVar()
        self.display.set("Wilkommen, dies ist ein deutlich längerer String zum testen.")
        self.label = ttk.Label(self.frame, textvariable=self.display, padding=1)
        self.label.grid(column=0, row=0, sticky="nwe")

        self.displayInv = tkinter.StringVar()
        self.displayInv.set("Inventar Teststring")
        self.labelInv = ttk.Label(self.frameInv, textvariable=self.displayInv, padding=5)
        self.labelInv.grid(column=0, sticky="n")

        self.user_input = ttk.Entry(self.mainframe, width=50, )
        self.user_input.bind("<Return>", lambda e: self.submit_button.invoke())
        self.user_input.grid(column=1, row=2, columnspan=2)

        self.submit_button = ttk.Button(self.mainframe, text="Bestätigen", command=self.update_display)
        self.submit_button.grid(column=1, row=3, columnspan=2)
        self.close_button = ttk.Button(self.mainframe, text="Programm schließen", command=self.window.destroy)
        self.close_button.grid(column=1, row=4, columnspan=2)
        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=1, sticky="e")
        self.load_button = ttk.Button(self.mainframe, text="Laden", command=self.save)
        self.load_button.grid(column=2, row=1, sticky="w")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        for child in self.window.winfo_children():
            for n in range(0, len(self.window.winfo_children())):
                child.columnconfigure(n, weight=1)
                child.rowconfigure(n, weight=1)
            for chil in child.winfo_children():
                for n in range(0, len(child.winfo_children())):
                    chil.columnconfigure(n, weight=1)
                    chil.rowconfigure(n, weight=1)

        self.mainframe.columnconfigure(0, weight=0)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, minsize=len(self.display.get()))

    def update_display(self):
        text = self.user_input.get()
        self.display.set(text)

    def save(self):
        save_data = (player, inventory, location)
        save = open("save.pickle", "wb")
        pickle.dump(save_data, save)
        time.sleep(0.5)
        save.close()

    def load(self):
        pass


#Global Variables
##############
forest = "in einem Wald."
cave = "in einer Höhle."
beach = "am Strand."

player = None
inventory = []
location = forest
##############

#Eigentlicher Programmablauf
window = tkinter.Tk()
program = MainGUI(window)


program.window.mainloop()
