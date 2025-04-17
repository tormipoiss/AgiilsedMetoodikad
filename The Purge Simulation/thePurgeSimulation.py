import random

class Player:
    def __init__(self,health,food,energy,time):
        self.health = health
        self.food = food
        self.energy = energy
        self.time = time


    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 2
            self.time -= 1
            self.makeSureRestWorks()
        else:
            print("Pole piisavalt toitu puhkamiseks.")

    def makeSureRestWorks(self):
        if self.food > 0 and self.energy > 0 and self.time > 0 and self.health > 0 and isinstance(self.food, int) and isinstance(self.energy, int) and isinstance(self.health, int) and isinstance(self.time, int):
            print("Rest töötab. Puhkasid ja said +2 energiat.")
        else:
            print("Rest ei tööta.")

    def status(self):
        print(f"Elu: {self.health}, Toit: {self.food}, Energia: {self.energy}, Aeg alles tundides: {self.time}")

    def event(self):
        if self.energy > 0:
            self.time -= 1
            self.energy -= 1
            event = random.choice(["leidsid toitu", "kohtusid vaenlasega", "leidsid varustust"])
            if event == "leidsid toitu":
                self.food += 2
                self.time -= 1
                print("Leidsid toitu! +2 toitu.")
            elif event == "kohtusid vaenlasega":
                self.health -= 5
                self.time -= 1
                print("Kohtusid vaenlasega! -5 elu.")
            elif event == "leidsid varustust":
                self.energy += 3
                self.time -= 1
                print("Leidsid varustust! +3 energiat.")
        else:
            print("Pole piisavalt energiat liikumiseks.")

    def riskEvent(self):
        if self.energy > 0:
            self.time -= 1
            self.energy -= 1
            risk = random.choice(["õnnestus", "nurjus"])
            if risk == "õnnestus":
                self.food += 5
                self.health += 10
                self.time -= 1
                print("Risk õnnestus! +5 toitu ja +10 elu.")
            else:
                self.health -= 10
                self.time -= 1
                print("Risk nurjus! -10 elu.")
        else:
            print("Pole piisavalt energiat liikumiseks.")

    def varu(self):
        if self.energy > 0:
            self.food += 1
            self.energy -= 1
            self.time -= 1
            print("Varusid ressursse. +1 toit ja -1 energia.")
        else:
            print("Pole piisavalt energiat varumiseks.")

print("Tere tulemast mängu!")
print("Mängu eesmärk on ellu jääda ja koguda ressursse.")

endGame = False
mängijaValitud = False

while endGame == False:
    while mängijaValitud == False:
        try:
            health = int(input("Vali mängija elu suurus: "))
            food = int(input("Vali mängija toidu suurus: "))
            energy = int(input("Vali mängija energia suurus: "))
            time = int(input("Vali mängija vajaliku ellujäämise aja pikkus (tundides): "))
            
            player = Player(health, food, energy, time)
            print("Mängija loodud! Mäng algab!")
            mängijaValitud = True
        except ValueError:
            print("Vale sisestus. Proovi uuesti. Kõik väärtused peavad olema täisarvud.")

    while True:
        if (player.health <= 0 or player.food <= 0 or player.energy <= 0):
            print("Mäng läbi! Sa oled surnud.")
            user_input = input("Mängu lõpetamiseks vajutage Enter, uue mängu alustamiseks sisestage R: ")
            if user_input.lower() == "r":
                mängijaValitud = False
                break
            else:
                print("Mäng lõpetatud.")
                endGame = True
                break
        if player.time <= 0:
            print("Aeg on otsas! Jäid ellu.")
            user_input = input("Mängu lõpetamiseks vajutage Enter, uue mängu alustamiseks sisestage R: ")
            if user_input.lower() == "r":
                mängijaValitud = False
                break
            else:
                print("Mäng lõpetatud.")
                endGame = True
                break
        valik = input("Kas soovid edasi liikuda / riskida / varuda ressursse / puhata / vaadata teavet / lõpetada mängu?\n"
                      "(liigu/riski/varu/puhka/vaata/lõpeta): ").lower()
        if valik == "liigu":
            player.event()
            player.status()
        elif valik == "riski":
            player.riskEvent()
            player.status()
        elif valik == "varu":
            player.varu()
            player.status()
        elif valik == "puhka":
            player.rest()
            player.status()
        elif valik == "vaata":
            player.status()
        elif valik == "lõpeta":
            print("Mäng lõpetatud.")
            endGame = True
            break
        else:
            print("Vale sisestus. Proovi uuesti.")