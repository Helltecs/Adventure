import tkinter
from tkinter import ttk
import pickle
import time
import random


class Weapon:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def upgrade(self):
        self.dmg += 1


class Person:
    def __init__(self, type, name: str, hp: int, strg, defe, equipW: Weapon, equipA):
        self.type = type
        self.name = name
        self.hp = hp
        self.strg = strg
        self.defe = defe
        self.equipW = equipW
        self.equipA = equipA

    def __str__(self):
        return self.name

    def equip(self, weapon_or_amor):
        if weapon_or_amor == Weapon:
            self.equipW = weapon_or_amor
        else:
            self.equipA = weapon_or_amor


class MainGUI:
    def __init__(self, mainWindow):
        self.first_load = True

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

        self.close_button = ttk.Button(self.mainframe, text="Programm schließen", command=self.window.destroy)
        self.close_button.grid(column=1, row=4, columnspan=2)
        self.new_game_button = ttk.Button(self.mainframe, text="Neues Spiel", command=self.new_game)
        self.new_game_button.grid(column=1, row=1, sticky="e")
        self.load_button = ttk.Button(self.mainframe, text="Laden", command=self.load)
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

    def new_game(self):
        self.user_input = ttk.Entry(self.mainframe, width=50)
        self.user_input.bind("<Return>", lambda e: self.submit_button.invoke())
        self.user_input.focus()
        self.user_input.grid(column=1, row=2, columnspan=2)

        self.submit_button = ttk.Button(self.mainframe, text="Bestätigen",
                                        command=self.get_player_name)
        self.submit_button.grid(column=1, row=3, columnspan=2)
        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=1, sticky="e")

        self.load_button.configure(state="disabled")

        self.display.set("Wilkommen!\n\nBitte trage deinen Namen unten in das Feld ein und bestätige deine Eingabe.")
        self.user_input.insert(0, "Hier Name eintragen")

        self.new_game_button.forget()

    def get_player_name(self):
        global player
        player = Person("player", self.user_input.get(), 100, 5, 5, None, None)
        self.display.set(f"Herzlich wilkommen {player}!\n\n")
        self.display_initial_prompt()
        self.user_input.destroy()
        self.submit_button.destroy()

    def update_display(self, text: str):
        self.display.set(text)

    def save(self):
        save_data = (player, inventory, location)
        save = open("save.pickle", "wb")
        pickle.dump(save_data, save)
        time.sleep(0.5)
        save.close()
        self.load_button.configure(state="active")

    def load(self):
        save = open("save.pickle", "rb")
        save_content = pickle.load(save)
        save.close()
        global player
        player = save_content[0]
        global inventory
        inventory = save_content[1]
        global location
        loacation = save_content[2]

        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=1, sticky="e")

        self.new_game_button.forget()

        if self.first_load:
            self.first_load = False
            self.update_display(f"Wilkommen zurück {player}!\n\n")
            self.display_initial_prompt()
        else:
            self.update_display("Du hast erneut geladen.")

    def display_initial_prompt(self):
            self.display.set(self.display.get() + f"Du befindest dich {location}")


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
