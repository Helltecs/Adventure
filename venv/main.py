import random







class Monster(Person):
   pass

def battle(strg, dmg, defe):
    if strg > dmg:
        temp = strg
        strg = dmg
        dmg = temp

    cal_dmg = random.randint(strg, dmg)
    cal_dmg -= defe
    print(f"Du hast: {cal_dmg} Schaden verursacht.\n")

    if cal_dmg >= 0:
        return cal_dmg
    else:
        return 0

def result(ergebnis, monsterHP):
    print(f"Das Monster hatte {monsterHP} Leben.")
    monsterHP -= ergebnis
    print(f"Das Monster hat nun: {monsterHP} Leben.\n")
    return monsterHP

def choose_location():
    while True:
        temp = input(
            "Tippe 'Wald' um zum Wald zu gehen, 'Höhle' um zur Höhle zu gehen und 'Strand', um zum Strand zu gehen.\n")
        if temp == "Wald":
            location = forest
            break
        elif temp == "Höhle":
            location = cave
            break
        elif temp == "Strand":
            location = beach
            break
        else:
            print("Versuche es nochmal. Achte auf die korrekte Schreibeweise.")
            time.sleep(1)
    return location

def loc(location):
    print(f"Du befindest dich {location}")

def ValidateInt(in_Here):
        try:
            int(in_Here)
            return True
        except ValueError:
            print("Keine Nummer")
            return False


def ValidateRange(list, int):
    try:
        if len(list) >= int:
            return True
        else:
            print("Achte darauf, dass sich die Nummer in der Liste befindet.")
            return False
    except IndexError:
        print("Achte darauf, dass sich die Nummer in der Liste befindet.")
        return False


window = tkinter.Tk()
window.geometry("900x450")
window.title("Text RPG")

frame = ttk.Frame(window, relief="sunken", padding=5)
frame.pack(side="top")
frameInv = ttk.Frame(window, relief="groove", padding=5)
frameInv.pack(anchor="nw", fill="y", expand=True)

display = tkinter.StringVar()
display.set("Wilkommen, dies ist ein deutlich längerer String zum testen.\n\n\n\n\n\n\n\n")
label = ttk.Label(frame, textvariable=display, padding=5)
label.grid(column=2, row=1)

displayInv = tkinter.StringVar()
displayInv.set("Invetar Teststring")
labelInv = ttk.Label(frameInv, textvariable=displayInv, padding=5)
labelInv.pack(side="top")

close_button = ttk.Button(window, text="Programm schließen", command=window.destroy)
close_button.pack(side="bottom", pady=20)

user_input = ttk.Entry(window, width=50)
user_input.pack()

window.mainloop()

#Umgebungen, fängt an mit "Du befindest dich ", verwende loc(string)



dagger = Weapon("Rückenstecher", 3)
monster = Monster("Ork", "Koklik", 10, 1, 1, None, None)


characters = []

start_up = True
begrüßung = None
save = None


while True: #Hauptschleife

    temp = None
    bool = False
    bool2 = False

    if start_up == True:
        temp = input("Hast du dieses Adventure schon einmal gespielt? (Y/N)\n")

        if temp.upper() == "Y":

            print(f"Wilkommen zurück {player}!")
            begrüßung = False
            start_up = False
        else:
            player = Person("player", input("Spielername: "), 100, 5, 5, None, None)
            inventory = [dagger]
            begrüßung = True
            start_up = False

    if begrüßung:
        print(f"Willkommen, {player.name}, bei diesem kleinen Adventure.")
        begrüßung = False
        time.sleep(3)

    loc(location)

    print("Was möchstest du als nächstes tun?")

    while not bool:
        temp = input("1. Möchtest du dein Inventar öffnen?\n2. Möchtest du dich an einen anderen Ort begeben?\n"
                     "3. Möchtest du dich umsehen?\nDrücke jede andere Ziffer um das Program zu beenden.\n")
        bool = ValidateInt(temp)

    temp = int(temp)

    if temp == 1:
        close = False
        counter = 1
        print(f"Du hast {len(inventory)} Gegenstände in deinem Inventar.\nListe der Gegenstände:")
        for item in inventory:
            print(f"{counter}. {item.name}")
            counter += 1

        while not close:
            temp = input("Möchtest du einen Gegenstand ausrüsten (1), entsorgen (endgültig)(2) oder das Inventar schließen(3)?\n")
            ValidateInt(temp)
            temp = int(temp)
            if temp == 1:
                bool = False
                bool2 = False
                while not bool or not bool2:
                    temp = input("Welchen Gegenstand möchtst du ausrüsten?\n")
                    bool = ValidateInt(temp)
                    bool2 = ValidateRange(inventory, int(temp))
                bool = False
                bool2 = False
                temp = int(temp) - 1
                player.equip(inventory[temp])

            elif temp == 2:
                bool = False
                bool2 = False
                while not bool or not bool2:
                    temp = input("Welchen Gegenstand möchtst du entsorgen?\n")
                    bool = ValidateInt(temp)
                    bool2 = ValidateRange(inventory, int(temp))
                bool = False
                bool2 = False
                temp = int(temp) - 1
                inventory.pop(temp)

            elif temp == 3:
                close = True
            else:
                print("Es werden nur die zur Verfügung stehenden Zahlen akzeptiert.")
                time.sleep(3)

    elif temp == 2:
       location = choose_location()

    elif temp == 3:
        print("Du siehst dich um.")
        if location == forest:
            print("Du findest Moos. Dir fällt ansonsten nichts besonderes auf.")
        elif location == cave:
            print("Außer Steine, erkennst du keine interessanten Gegenstände.")
        elif location == beach:
            print(f"Du triffst auf {monster.name}. {monster.name} ist ein {monster.type}.")
            time.sleep(3)

            while player.hp and monster.hp > 0:
                ergebnis = battle(player.strg, dagger.dmg, monster.defe)
                monster.hp = result(ergebnis, monster.hp)
                time.sleep(1.5)

            print(f"\nGlückwunsch, du hast den unschuldigen {monster.name} getötet. :(\n")

    else:

        break

