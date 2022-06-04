import tkinter
from tkinter import ttk

class MainGUI:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.window.geometry("900x450")
        self.window.title("Text RPG")
        self.mainframe = ttk.Frame(self.window, padding=10)
        self.mainframe.grid(column=0, row=0, sticky="wnse")
        self.frame = ttk.Frame(self.mainframe, borderwidth=5, relief="sunken", padding=5)
        self.frame.grid(column=1, row=0, sticky="wnse", pady=(0, 5))
        self.frameInv = ttk.Frame(self.mainframe, relief="groove", padding=5)
        self.frameInv.grid(column=0, row=0, rowspan=3, sticky="ns")

        self.display = tkinter.StringVar()
        self.display.set("Wilkommen, dies ist ein deutlich längerer String zum testen.")
        self.label = ttk.Label(self.frame, textvariable=self.display, padding=1)
        self.label.grid(column=0, row=0, sticky="nwe")

        self.displayInv = tkinter.StringVar()
        self.displayInv.set("Invetar Teststring")
        self.labelInv = ttk.Label(self.frameInv, textvariable=self.displayInv, padding=5)
        self.labelInv.grid(column=0, sticky="n")

        self.user_input = ttk.Entry(self.mainframe, width=50, )
        self.user_input.bind("<Return>", lambda e: self.submit_button.invoke())
        self.user_input.grid(column=1, row=1)

        self.submit_button = ttk.Button(self.mainframe, text="Bestätigen", command=self.update_helper)
        self.submit_button.grid(column=1, row=2)
        self.close_button = ttk.Button(self.mainframe, text="Programm schließen", command=self.window.destroy)
        self.close_button.grid(column=1, row=3)

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

        self.mainframe.columnconfigure(1, weight=5)
        self.mainframe.rowconfigure(0, weight=5)
        self.frame.columnconfigure(0, minsize=len(self.label["text"]))

        test = ttk.Label(self.frame, text=self.user_input.get())
        test.grid()

    def update_display(self, Text: str):
        self.display.set(Text)

    def update_helper(self):
        text = self.user_input.get()
        self.update_display(text)


#Eigentlicher Programmablauf
window = tkinter.Tk()
program = MainGUI(window)

# Teste Git Version Control
program.window.mainloop()
