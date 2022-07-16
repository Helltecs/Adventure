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


class Monster:
    def __init__(self, type, name: str, hp: int, strg, defe):
        self.type = type
        self.name = name
        self.hp = hp
        self.strg = strg
        self.defe = defe

    def __str__(self):
        return self.name


class StatusWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("300x200+10+10")
        self.window.title("Charakterstatus")
        self.mainframe = ttk.Frame(self.window)
        self.mainframe.grid(column=0, row=0, sticky="nesw")

        ttk.Label(self.mainframe, text=f"Dein Name: {player}").pack(anchor="center")
        ttk.Label(self.mainframe, text=f"Lebenspunkte: {player.hp}").pack(anchor="center")
        ttk.Label(self.mainframe, text=f"Stärke: {player.strg}").pack(anchor="center")
        ttk.Label(self.mainframe, text=f"Verteidigung: {player.defe}").pack(anchor="center")


class MainGUI:
    def __init__(self, mainWindow):
        self.first_load = True
        self.inventory_button_list = []
        self.variable_list = []
        self.forest_image = tkinter.PhotoImage(file="Resources/forest.png")

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
        self.label = ttk.Label(self.frame, textvariable=self.display, padding=1, image=self.forest_image,
                               compound="center", foreground="white")
        self.label.grid(column=0, row=0, sticky="nwe")

        self.displayInv = tkinter.StringVar()
        self.displayInv.set("Inventar")
        self.labelInv = ttk.Label(self.frameInv, textvariable=self.displayInv, padding=5)
        self.labelInv.grid(column=0, sticky="n")
        self.goldVar = tkinter.StringVar()
        self.goldVar.set(f"Gold: {gold}")
        self.labelGold = ttk.Label(self.frameInv, textvariable=self.goldVar)
        self.labelGold.grid(column=0, row=len(self.inventory_button_list)+1, sticky="w")

        self.close_button = ttk.Button(self.mainframe, text="Programm schließen", command=self.window.destroy)
        self.close_button.grid(column=1, row=5, columnspan=2)
        self.new_game_button = ttk.Button(self.mainframe, text="Neues Spiel", command=self.new_game)
        self.new_game_button.grid(column=1, row=2, sticky="e")
        self.load_button = ttk.Button(self.mainframe, text="Laden", command=self.load)
        self.load_button.grid(column=2, row=2, sticky="w")
        self.forest_button = ttk.Button(self.location_frame, text="Wald", command=lambda: self.change_location("forest"),
                                        state="disabled")
        self.forest_button.grid(column=0, row=0, sticky="we")
        self.cave_button = ttk.Button(self.location_frame, text="Höhle", command=lambda: self.change_location("cave"),
                                      state="disabled")
        self.cave_button.grid(column=1, row=0, sticky="we")
        self.beach_button = ttk.Button(self.location_frame, text="Strand", command=lambda: self.change_location("beach"),
                                       state="disabled")
        self.beach_button.grid(column=2, row=0, sticky="we")
        self.discover_button = ttk.Button(self.location_frame, text="Umsehen", command=self.discover)
        self.nothing_button = ttk.Button(self.location_frame, text="Nichts tun", command=self.restore_location_buttons)
        self.fight_button = ttk.Button(self.location_frame, text="Kämpfen", command=self.fight)
        self.flee_button = ttk.Button(self.location_frame, text="Flüchten", command=self.flee_confirmation)
        self.status_button = ttk.Button(self.mainframe, text="Status", command=self.open_statuswindow)
        self.status_button.grid(column=0, row=1, sticky="n")

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

        self.new_game_button.destroy()
        self.update_inventory()

    def get_player_name(self):
        global player
        player = Person("player", self.user_input.get(), 100, 5, 5, None, None)
        self.display.set(f"Herzlich wilkommen {player}!\n\n")
        self.display_initial_prompt()
        self.user_input.destroy()
        self.submit_button.destroy()

        self.forest_button.configure(state="active")
        self.cave_button.configure(state="active")
        self.beach_button.configure(state="active")

    def update_display(self, text: str):
        self.display.set(text)

    def save(self):
        save_data = (player, inventory, gold, location)
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
        global gold
        gold = save_content[2]
        global location
        location = save_content[3]

        self.save_button = ttk.Button(self.mainframe, text="Speichern", command=self.save)
        self.save_button.grid(column=1, row=2, sticky="e")

        self.forest_button.configure(state="active")
        self.cave_button.configure(state="active")
        self.beach_button.configure(state="active")

        self.new_game_button.destroy()

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

        self.goldVar.set(f"Gold: {gold}")
        self.labelGold.grid_configure(row=len(self.inventory_button_list)+1)

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
        self.choose_action()

    def choose_action(self):
        self.forest_button.grid_remove()
        self.cave_button.grid_remove()
        self.beach_button.grid_remove()

        self.discover_button.grid(column=0, row=0)
        self.nothing_button.grid(column=1, row=0)

    def restore_location_buttons(self):
        self.discover_button.grid_remove()
        self.nothing_button.grid_remove()
        self.fight_button.grid_remove()
        self.flee_button.grid_remove()

        self.forest_button.grid()
        self.cave_button.grid()
        self.beach_button.grid()

    def discover(self):
        self.discover_button.grid_remove()
        self.nothing_button.grid_remove()

        dice = random.randint(1, 11)

        if location == forest:
            self.update_display("Dies ist ein Testevent für den Wald. Hier ist noch nicht viel zu sehen.\n\n")
            if dice <= 3:
                self.update_display(f"{self.display.get()}Du triffst auf einen Gegner.")
                global monster
                monster = self.create_monster()
                self.fight_button.grid(column=0, row=0)
                self.flee_button.grid(column=1, row=0)
                self.update_display(f"{self.display.get()}\n\nDu triffst auf {monster}. "
                                    f"{monster} ist ein {monster.type}.")
            elif 6 >= dice > 3:
                self.update_display(f"{self.display.get()}Du hast nichts entdeckt bzw. neutrales Event.")
                dice = random.randint(0, 4)
                self.update_display(f"{self.display.get()}\n\n{Events_Forest_Neutral[dice]}")
                self.restore_location_buttons()
            else:
                self.update_display(f"{self.display.get()}Du entdeckst ein Item oder ein sonstiges positives Event.")
                self.restore_location_buttons()
        elif location == cave:
            self.update_display("Dies ist ein Testevent für die Höhle. Hier ist noch nicht viel zu sehen.\n\n")
            if dice <= 3:
                self.update_display(f"{self.display.get()}Du triffst auf einen Gegner (noch zu implementieren).")
                self.restore_location_buttons()
            elif 6 >= dice > 3:
                #TODO Event strings in Textdatei/Listen schreiben, aufruf über Index
                self.update_display(f"{self.display.get()}Du hast nichts entdeckt bzw. neutrales Event.")
                self.restore_location_buttons()
            else:
                self.update_display(f"{self.display.get()}Du entdeckst ein Item oder ein sonstiges positives Event.")
                self.restore_location_buttons()
        elif location == beach:
            self.update_display("Dies ist ein Testevent für den Strand. Hier ist noch nicht viel zu sehen.\n\n")
            if dice <= 3:
                self.update_display(f"{self.display.get()}Du triffst auf einen Gegner (noch zu implementieren).")
                self.restore_location_buttons()
            elif 6 >= dice > 3:
                #TODO Event strings in Textdatei/Listen schreiben, aufruf über Index
                self.update_display(f"{self.display.get()}Du hast nichts entdeckt bzw. neutrales Event.")
                self.restore_location_buttons()
            else:
                self.update_display(f"{self.display.get()}Du entdeckst ein Item oder ein sonstiges positives Event.")
                self.restore_location_buttons()

    def fight(self):
        dmg_to_monster, dmg_to_player = calculate_battle(player.strg, player.defe, player.equippedW,
                                                         player.equippedW2, monster.strg, monster.defe)
        monster.hp -= dmg_to_monster
        player.hp -= dmg_to_player

        if monster.hp <= 0:
            self.display.set(f"Sehr gut! Du hast {monster} besiegt.")
            dice = random.randint(1, 6)
            if dice < 3:
                self.display.set(f"{self.display.get()}\n\nLeider hat das Monster nichts gedroppt.")
            elif 2 < dice < 5:
                self.display.set(f"{self.display.get()}\n\nDas Monster hat etwas Gold fallen lassen.")
                global gold
                gold += random.randint(1, 100)
                self.update_inventory()
            else:
                self.display.set(f"{self.display.get()}\n\nDas Monster hat einen Gegenstand fallen lassen.")
                # TODO Implementiere Itemdrop und hinzufügen zu Inventar
            self.restore_location_buttons()
        else:
            self.display.set(
                f"{self.display.get()}\n\nDu hast {dmg_to_monster} Schaden verursacht. {monster} hat bei dir "
                f"{dmg_to_player} Schaden verursacht.\nDu hast nun noch {player.hp} Lebenspunkte übrig, wärend"
                f" {monster} noch {monster.hp} Lebenspunkte übrig hat.")

    def flee_confirmation(self):
        self.flee_confirmation_window = tkinter.Tk()
        ttk.Label(self.flee_confirmation_window, text="Beim Fliehen besteht eine 30%ige Chance, 10% der derzeitigen Lebenspunkte zu verlieren."
                               "Möchtest du dennoch fliehen?").pack()
        ttk.Button(self.flee_confirmation_window, text="Fliehen", command=self.flee).pack()
        ttk.Button(self.flee_confirmation_window, text="Abbrechen", command=self.flee_confirmation_window.destroy).pack()

    def flee(self):
        self.flee_confirmation_window.destroy()
        global player
        if random.randint(1, 10) <= 3:
            player.hp -= player.hp * 0.1
            self.display.set("Du bist entkommen, hast aber bei der Flucht leider etwas Schaden bekommen.")
        else:
            self.display.set("Du bist entkommen.")
        self.restore_location_buttons()

    def create_monster(self):
        temp = random.choice(Monster_Types)
        if temp == "Ork":
            return Monster(temp, random.choice(Monster_Names[0]), 10, 5, 5)
        elif temp == "Imp":
            return Monster(temp, random.choice(Monster_Names[1]), 8, 3, 3)
        elif temp == "Zombie":
            return Monster(temp, random.choice(Monster_Names[2]), 5, 2, 2)
        else:
            print("Fehler bei 'create_monster'.")

    def open_statuswindow(self):
        StatusWindow()


def calculate_battle(strg, defe, dmg, dmg2, monsterstrg, monsterdefe):
    # Player strength, weapon damage, monster defense
    try:
        dmg = dmg.dmg
        dmg2 = dmg2.dmg
    except AttributeError:
        try:
            dmg = dmg.dmg
        except AttributeError:
            dmg = None
        try:
            dmg2 = dmg2.dmg
        except AttributeError:
            dmg2 = None

    if type(dmg) is not int and type(dmg) is not float:
        dmg = 0
    if type(dmg2) is not int and type(dmg2) is not float:
        dmg2 = 0

    dmg += dmg2

    if strg > dmg:
        temp = strg
        strg = dmg
        dmg = temp

    cal_dmg_to_monster = random.randint(strg, dmg)
    cal_dmg_to_monster -= monsterdefe
    cal_dmg_to_player = monsterstrg - defe

    if cal_dmg_to_monster >= 0 and cal_dmg_to_player >= 0:
        return cal_dmg_to_monster, cal_dmg_to_player
    elif cal_dmg_to_monster >= 0 and cal_dmg_to_player <= 0:
        return cal_dmg_to_monster, 0
    elif cal_dmg_to_monster <= 0 and cal_dmg_to_player >= 0:
        return 0, cal_dmg_to_player
    else:
        return 0, 0


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
monster = None
inventory = [dagger, tatters, testw1, testw2, testw3, testw4]
gold = 0
location = forest

with open("Resources/Event_Forest_Neutral", "r", encoding="utf-8") as t:
    Events_Forest_Neutral = t.readlines()
    t.close()
for i in Events_Forest_Neutral:
    t = i.replace("\\n", "\n").rstrip("\n")
    Events_Forest_Neutral.pop(0)
    Events_Forest_Neutral.append(t)

with open("Resources/Monster_Types", "r", encoding="utf-8") as t:
    Monster_Types = t.readlines()
    t.close()
for i in Monster_Types:
    Monster_Types.append(i.replace("\n", ""))
    Monster_Types.pop(0)

with open("Resources/Monster_Names", "r", encoding="utf-8") as t:
    Monster_Names = t.readlines()
    t.close()
for i in Monster_Names:
    Monster_Names.append(Monster_Names[0].split())
    Monster_Names.pop(0)
##############

#Eigentlicher Programmablauf
window = tkinter.Tk()
program = MainGUI(window)
program.window.mainloop()
