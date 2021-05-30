import random

#digilist
Stage1 = ["Botamon","Poyomon","Punimon","Yuramon"]
Stage2 = ["Koromon","Tokomon","Tsunomon","Tanemon"]
Stage3 = ["Gabumon", "Biyomon", "Agumon","Patamon","Elecmon","Penguinmon","Palmon","Betamon"]
Stage4 = ["Greymon", "Meramon", "Birdramon", "Centarumon", "Monochromon", "Tyranomon", "Devimon", "Ogremon","Leomon","Angemon","Airdramon","Kokatorimon","Unimon","Kabuterimon",
"Ninjamon","Seadramon","Whamon","Shellmon","Mojyamon","Frigimon","Garurumon","Vegiemon","Bakemon","Drimogemon","Coelamon","Kuwagamon"]


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

    #In-training 1
    if mon == "Botamon" and O|D|S|B > 2:
        mon = "Koromon"
        print ("{0} has evolved into {1}".format(name,mon)  )

    if mon == "Poyomon" and O|D|S|B > 2:
        mon = "Tokomon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Punimon" and O|D|S|B > 2:
        mon = "Tsunomon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Yuramon" and O|D|S|B > 2:
        mon = "Tanemon"
        print ("{0} has evolved into {1}".format(name,mon))

    #In-training 2
    if mon == "Koromon" and O > 10 and D&S&B >5:
        mon = "Agumon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Koromon" and O&B >5 and D&S>10 :
        mon = "Gabumon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tokomon" and O&B >10 and D&S >5:
        mon = "Patamon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tokomon" and O&D&B >5 and S >10:
        mon = "Biyomon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tsunomon" and O|S > 9:
        mon = "Elecmon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tsunomon" and D|B > 9:
        mon = "Penguinmon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tanemon" and B > 9:
        mon = "Palmon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Tanemon" and D > 9:
        mon = "Betamon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Kunemon - Null

    #Champion
    if mon == "Agumon" and O&D&S&B >20:
        mon = "Greymon"
        print ("{0} has evolved into {1}".format(name,mon))
        
    if mon == "Agumon" and O >25 and D&S&B >15:
        mon = "Meramon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Agumon" or "Biyomon") and S >25:
        mon = "Birdramon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Agumon" or "Gabumon") and B >25:
        mon = "Centarumon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Agumon" or "Gabumon") and D >25 and B >20:
        mon = "Monochromon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Gabumon" or "Patamon") and O >25:
        mon = "Drimogemon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == "Penguinmon" and B >20:
        mon = "Frigimon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Agumon" or "Gabumon" or "Patamon") and D >20:
        mon = "Tyranomon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Devimon - Null

    if mon == ("Gabumon" or "Patamon") and O >25:
        mon = "Ogremon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Patamon" or "Elecmon") and O >25 and S&B >20:
        mon = "Leomon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Patamon" or "Elecmon") and B >25:
        mon = "Angemon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Bakemon - Null

    #Mojyamon - Null

    if mon == "Biyomon" and speed > 20 and B >20:
        mon = "Airdramon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Kokatorimon - Null

    if mon == ("Patamon" or "Biyomon") and S >20:
        mon = "Unimon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Biyomon" or "Kunemon") and O&D&S >20:
        mon = "Kabuterimon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Kunemon" or "Palmon") and O&S >20:
        mon = "Kuwagumon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Vegiemon - Null

    if mon == "Palmon" and O&S >20:
        mon = "Ninjamon"
        print ("{0} has evolved into {1}".format(name,mon))

    #Seadramon - Null

    if mon == ("Palmon" or "Betamon" or "Penguinmon") and B >20:
        mon = "Whamon"
        print ("{0} has evolved into {1}".format(name,mon))
    
    if mon == ("Betamon" or "Penguinmon") and D >25:
        mon = "Shellmon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Palmon" or "Betamon") and D >20:
        mon = "Coelamon"
        print ("{0} has evolved into {1}".format(name,mon))

    if mon == ("Gabumon" or "Penguinmon") and D >20:
        mon = "Garurumon"
        print ("{0} has evolved into {1}".format(name,mon))