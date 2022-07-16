import random







class Monster:
   pass




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




#Umgebungen, fängt an mit "Du befindest dich ", verwende loc(string)



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
            player = None
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
                player.equip_else_unequip(inventory[temp])

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

