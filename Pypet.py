from hashlib import new
import random

#digilist
Stage1 = ["Botamon","Poyomon","Punimon","Yuramon"]
Stage2 = ["Koromon","Tokomon","Tsunomon","Tanemon"]
Stage3 = ["Gabumon", "Biyomon", "Agumon","Patamon","Elecmon","Penguinmon","Palmon","Betamon"]
Stage4 = ["Greymon", "Meramon", "Birdramon", "Centarumon", "Monochromon", "Tyranomon", "Devimon", "Ogremon","Leomon","Angemon","Airdramon","Kokatorimon","Unimon","Kabuterimon",
"Ninjamon","Seadramon","Whamon","Shellmon","Mojyamon","Frigimon","Garurumon","Vegiemon","Bakemon","Drimogemon","Coelamon","Kuwagamon"]

#Class
class Digi:
    def __init__(self,mon,age,offense,defense,speed,brains,evo):
        self.mon = mon
        self.age = age
        self.offense = offense
        self.defense = defense
        self.speed = speed
        self.brains = brains
        self.evo = evo
    #def __eq__(self, Digi: object):
    #    if self.mon == object.evo and self.offense >= object.offense and self.defense >= object.defense and self.speed >= object.speed and self.brains >= object.brains:       
    #        return

D1 = Digi("Botamon",0,1,1,1,1,"")
D2 =
D3 =
D4 =
D3 = Digi("Koromon",1,5,5,5,5,"Botamon")
D4 = Digi("Agumon",2,15,10,10,10,"Koromon")

Digilist = [D1,D2,D3]

self = D1
name = self.mon

#Base Stats


def Evo(): 
    for obj in Digilist: 
        if obj.evo == self.mon and self.offense >= obj.offense and self.defense >= obj.defense and self.speed >= obj.speed and self.brains >= obj.brains:
            self.mon = obj.mon
            print("{0} has evolved into {1}".format(name,self.mon))
            return


def startup_pypet():
    print("Welcome to Pypet!\nLet's start with naming your {0}.\nType 'name' to give your {0} a name".format(self.mon))

def pypet_stats():
    #print("{0} weighs {1} pounds".format(name,weight))
    print("{0} has {1} offense".format(name,self.offense))
    print("{0} has {1} defense".format(name,self.defense))
    print("{0} has {1} speed".format(name,self.speed))
    print("{0} has {1} brains".format(name,self.brains))
    print("{0} is a {1}".format(name,self.mon))

    #if food < 3:
    #    print("{0} is hungry!".format(name))
    #elif food <5:
    #    print("{0} could eat".format(name))
    #else:
    #    print("{0} is full!".format(name))

#training
def train():
    print("Which stat would you like to train?")
    print("Offense = {0}".format(self.offense))
    print("Defense = {0}".format(self.defense))
    print("Speed = {0}".format(self.speed))    
    print("Brains = {0}".format(self.brains))
    user_input = input("> ")

    if user_input == "offense":
        gain = random.randint(1,5)
        self.offense = self.offense + gain
        #food = food -1
        print("{0}'s offense increased by {2}.\n{0}'s offense is now {1}".format(name,self.offense,gain))
        Evo()
        return

    elif user_input == "defense":
        self.defense = self.defense +random.randint(1,5)
        #food = food -1
        print("{0}'s defense increaded to {1}".format(name,self.defense))
        Evo()
        return

    elif user_input == "speed":
        self.speed = self.speed +random.randint(1,5)
        #food = food -1
        print("{0}'s speed increaded to {1}".format(name,self.speed))
        Evo()
        return

    elif user_input == "brains":
        self.brains = self.brains +random.randint(1,5)
        #food = food -1
        print("{0}'s brains increaded to {1}".format(name,self.brains))
        Evo()
        return

    else: 
        print("please select which stat you would like to train")
        return


#Startup
startup_pypet()
Digi


terminate = False
#whileloop
while not terminate:
    print("#########################")

    #General Input
    user_input = input('> ')

    if user_input == "quit":
        terminate = True
        print("Goodbye")
    
    elif user_input == "commands":
        print("'Quit' to close\n'Name' to rename {0}\n'Stats' to see {0}'s stats\n'Feed' to feed {0}\n'Train' to improve {0}'s stats".format(name))

    elif user_input == "name":
        user_input = input("Enter a name for {0} > ".format(name))
        name = user_input
            
    elif user_input == "stats":
        pypet_stats()

    #elif user_input == "feed":
    #    weight = weight + 1
    #    food = food + 1
    #    if food <3:
    #        print("You fed {0}, but they are still hungry!".format(name))

#       elif food <5:
#            food = food +1
#            print ("You fed {0}".format(name))
         
#        else:
#            print(self.mon +" is stuffed and can't eat anymore!")

    elif user_input == "train":
        train()

    else:
        print("Sorry there was an error. Type 'commands' to see a list of valid commands")

    #Evolutions
   