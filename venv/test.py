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


class Armor:
    def __init__(self, name, defe):
        self.name = name
        self.defe = defe

    def upgrade(self):
        self.defe += 1


class Person:
    def __init__(self, type, name: str, hp: int, strg, defe, equippedW: Weapon, equippedA: Armor):
        self.type = type
        self.name = name
        self.hp = hp
        self.strg = strg
        self.defe = defe
        self.equippedW = equippedW
        self.equippedW2 = None
        self.equippedA = equippedA

    def __str__(self):
        return self.name

    def equip_else_unequip(self, weapon_or_armor):
        print("Aufgerufen")
        if type(weapon_or_armor) == type(dagger) and self.equippedW == None:
            self.equippedW = weapon_or_armor
            print("Ausgeführt 1")
        elif type(weapon_or_armor) == type(dagger) and self.equippedW2 == None:
            self.equippedW2 = weapon_or_armor
            print("Ausgeführt 2")
        elif type(weapon_or_armor) == type(tatters) and self.equippedA == None:
            self.equippedA = weapon_or_armor
            print("Ausgeführt 4")
        else:
            self.unequip(weapon_or_armor)
            print("Ausgeführt 5")
        program.update_inventory()
        print(self.equippedW, self.equippedW2, self.equippedA)

    def unequip(self, weapon_or_armor):
        print("Ebenfalls aufgerufen")
        if type(weapon_or_armor) == type(dagger):
            if self.equippedW != None:
                if weapon_or_armor.name == self.equippedW.name:
                    self.equippedW = None
                    print("Ausgeführt 6")
                else:
                    pass
            elif self.equippedW2 != None:
                self.equippedW2 = None
                print("Ausgeführt 7")
            else:
                print("Ausgeführt 8")
                pass
        else:
            self.equippedA = None
            print("Ausgeführt 9")
        print(self.equippedW, self.equippedW2, self.equippedA)


class MainGUI:
    def __init__(self, mainWindow):
        self.first_load = True
        self.inventory_button_list = []
        self.variable_list = []

        self.window = mainWindow
        self.window.geometry("900x450")
        self.window.title("Text RPG")
        self.mainframe = ttk.Frame(self.window, padding=10)
        self.mainframe.grid(column=0, row=0, sticky="wnse")
        self.frame = ttk.Frame(self.mainframe, borderwidth=5, relief="sunken", padding=5)
        self.frame.grid(column=1, row=0, sticky="nwe", pady=(0, 5), columnspan=2)
        self.frameInv = ttk.Frame(self.mainframe, relief="groove", padding=5)
        self.frameInv.grid(column=0, row=0, sticky="n")
        self.location_frame = ttk.Frame(self.mainframe, relief="ridge", padding=5)
        self.location_frame.grid(column=1, row=1, sticky="n", columnspan=2)

        self.display = tkinter.StringVar()
        self.display.set("Wilkommen, dies ist ein deutlich längerer String zum testen.")
        self.label = ttk.Label(self.frame, textvariable=self.display, padding=1)
        self.label.grid(column=0, row=0, sticky="nwe")

        self.displayInv = tkinter.StringVar()
        self.displayInv.set("Inventar")
        self.labelInv = ttk.Label(self.frameInv, textvariable=self.displayInv, padding=5)
        self.labelInv.grid(column=0, sticky="n")

        self.close_button = ttk.Button(self.mainframe, text="Programm schließen", command=self.window.destroy)
        self.close_button.grid(column=1, row=5, columnspan=2)
        self.new_game_button = ttk.Button(self.mainframe, text="Neues Spiel", command=self.new_game)
        self.new_game_button.grid(column=1, row=2, sticky="e")
        self.load_button = ttk.Button(self.mainframe, text="Laden", command=self.load)
        self.load_button.grid(column=2, row=2, sticky="w")
        self.forest_button = ttk.Button(self.location_frame, text="Wald", command=lambda: self.change_location("forest"))
        self.forest_button.grid(column=0, row=0, sticky="we")
        self.cave_button = ttk.Button(self.location_frame, text="Höhle", command=lambda: self.change_location("cave"))
        self.cave_button.grid(column=1, row=0, sticky="we")
        self.beach_button = ttk.Button(self.location_frame, text="Strand", command=lambda: self.change_location("beach"))
        self.beach_button.grid(column=2, row=0, sticky="we")

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
        self.user_input.grid(column=1, row=3, columnspan=2)

        self.submit_button = ttk.Button(self.mainframe, text="Bestätigen",
                                        command=self.get_player_name)
        self.submit_button.grid(column=1, row=4, columnspan=2)
        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=2, sticky="e")

        self.load_button.configure(state="disabled")

        self.display.set("Wilkommen!\n\nBitte trage deinen Namen unten in das Feld ein und bestätige deine Eingabe.")
        self.user_input.insert(0, "Hier Name eintragen")

        self.new_game_button.forget()
        self.update_inventory()

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
        location = save_content[2]

        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=2, sticky="e")

        self.new_game_button.forget()

        self.update_inventory()

        if self.first_load:
            self.first_load = False
            self.update_display(f"Wilkommen zurück {player}!\n\n")
            self.display_initial_prompt()
        else:
            self.update_display("Du hast erneut geladen.")

    def display_initial_prompt(self):
            self.display.set(self.display.get() + f"Du befindest dich {location}")

    def update_inventory(self):
        count = 0
        if len(inventory) != len(self.inventory_button_list):
            for item in inventory:
                temp = tkinter.IntVar()
                temp.set(0)
                self.variable_list.append(temp)
                self.inventory_button_list.append(ttk.Checkbutton(self.frameInv, text=item.name,
                                                                  variable=self.variable_list[count],
                                                                  command=self.button_checked))
                self.inventory_button_list[count].grid(row=count + 1, sticky="ew")
                count += 1
        added = 0
        for value in self.variable_list:
            added += value.get()
        count = 0
        for box in self.inventory_button_list:
            if added >= 2 and self.variable_list[count].get() == 0:
                box.configure(state="disabled")
            else:
                box.configure(state="active")
            count += 1

    def button_checked(self):
        count = 0
        for box in self.inventory_button_list:
            if self.variable_list[count].get() == 1:
                for item in inventory:
                    if item.name == box["text"]:
                        player.equip_else_unequip(item)
                    else:
                        continue
            else:
                for item in inventory:
                    if item.name == box["text"]:
                        player.unequip(item)
            count += 1

    def change_location(self, goal):
        global location
        if goal == "forest":
            location = forest
        elif goal == "cave":
            location = cave
        elif goal == "beach":
            location = beach
        self.update_display(f"Du befindest dich {location}" + "\n\nWas möchtest du tun?")


#Global Variables
##############
dagger = Weapon("Rückenstecher", 3)
testw1 = Weapon("Test 1", 3)
testw2 = Weapon("Test 2", 3)
testw3 = Weapon("Test 3", 3)
testw4 = Weapon("Test 4", 3)

tatters = Armor("Lumpen", 1)

forest = "in einem Wald."
cave = "in einer Höhle."
beach = "am Strand."

player = None
inventory = [dagger, tatters, testw1, testw2, testw3, testw4]
location = forest
##############

#Eigentlicher Programmablauf
window = tkinter.Tk()
program = MainGUI(window)
program.window.mainloop()
