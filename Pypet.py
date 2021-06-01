import random

#digilist
Stage1 = ["Botamon","Poyomon","Punimon","Yuramon"]
Stage2 = ["Koromon","Tokomon","Tsunomon","Tanemon"]
Stage3 = ["Gabumon", "Biyomon", "Agumon","Patamon","Elecmon","Penguinmon","Palmon","Betamon"]
Stage4 = ["Greymon", "Meramon", "Birdramon", "Centarumon", "Monochromon", "Tyranomon", "Devimon", "Ogremon","Leomon","Angemon","Airdramon","Kokatorimon","Unimon","Kabuterimon",
"Ninjamon","Seadramon","Whamon","Shellmon","Mojyamon","Frigimon","Garurumon","Vegiemon","Bakemon","Drimogemon","Coelamon","Kuwagamon"]

#Class
class Digi:
    def __init__(self,mon,age,O,D,S,B,evo):
        self.mon = mon
        self.age = age
        self.offense = O
        self.defense = D
        self.speed = S
        self.brains = B
        self.evo = evo
    def __eq__(self,other):
        if self.mon == other.evo and self.offense == other.O and self.defense == other.D and self.speed == other.S and self.brains == other.B:
            self.mon = other.mon
            print("{0} has evolved into {1}")
            pass
class S1(Digi):
    pass
class S2(Digi):
    pass
class S3(Digi):
    pass
class S4(Digi):
    pass




#stage1
D1 = S1("Botamon",0,1,1,1,1,"")
D2 = S1("Poyomon",0,1,1,1,1,"")
D3 = S1("Punimon",0,1,1,1,1,"")
D4 = S1("Yuramon",0,1,1,1,1,"")
#Stage2
D5 = S2("Koromon",1,5,5,5,5,"Botamon")
D6 = S2("Tokomon",1,5,5,5,5,"Poyomon")
D7 = S2("Tsunomon",1,5,5,5,5,"Punimon")
D8 = S2("Tanemon",1,5,5,5,5,"Yuramon")
#Stage3
#D9 = S3("Gabumon",2,5,10,10,5)
#D10 = S3("Biyomon",2,5,5,10,5)
#D11 = S3()

#Base Stats
mon = random.choice(Stage1)
name = mon
age = 0
weight = 2
offense = 1
defense = 1
speed = 1
brains = 1
food = 5


def startup_pypet():
    print("Welcome to Pypet!\nLet's start with naming your {0}.\nType 'name' to give your {0} a name".format(mon))

def pypet_stats():
    print("{0} weighs {1} pounds".format(name,weight))
    print("{0} has {1} offense".format(name,offense))
    print("{0} has {1} defense".format(name,defense))
    print("{0} has {1} speed".format(name,speed))
    print("{0} has {1} brains".format(name,brains))
    print("{0} is a {1}".format(name,mon))

    if food < 3:
        print("{0} is hungry!".format(name))
    elif food <5:
        print("{0} could eat".format(name))
    else:
        print("{0} is full!".format(name))

#training
def train():
    global offense
    global defense
    global speed
    global brains
    global food
    print("Which stat would you like to train?")
    print("Offense = {0}".format(offense))
    print("Defense = {0}".format(defense))
    print("Speed = {0}".format(speed))    
    print("Brains = {0}".format(brains))
    user_input = input("> ")

    if user_input == "offense":
        offense = offense +random.randint(1,5)
        food = food -1
        print("{0}'s offense increased to {1}".format(name,offense))
        return

    elif user_input == "defense":
        defense = defense +random.randint(1,5)
        food = food -1
        print("{0}'s defense increaded to {1}".format(name,defense))
        return

    elif user_input == "speed":
        speed = speed +random.randint(1,5)
        food = food -1
        print("{0}'s speed increaded to {1}".format(name,speed))
        return

    elif user_input == "brains":
        brains = brains +random.randint(1,5)
        food = food -1
        print("{0}'s brains increaded to {1}".format(name,brains))
        return

    else: 
        print("please select which stat you would like to train")
        return


#Startup
startup_pypet()



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
        user_input = input("Enter a name for {0} > ".format(mon))
        name = user_input
            
    elif user_input == "stats":
        pypet_stats()

    elif user_input == "feed":
        weight = weight + 1
        food = food + 1
        if food <3:
            print("You fed " + mon + ", but they are still hungry!")

        elif food <5:
            food = food +1
            print ("You fed your " + mon)
         
        else:
            print(mon +" is stuffed and can't eat anymore!")

    elif user_input == "train":
        train()

    else:
        print("Sorry there was an error. Type 'commands' to see a list of valid commands")

    O = offense
    D = defense
    S = speed
    B = brains

    #Evolutions
   