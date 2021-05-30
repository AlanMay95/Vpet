import random



#digilist
Stage1 = ["Botamon","Poyomon","Punimon","Yuramon"]
Stage2 = ["Koromon","Tokomon","Tsunomon","Tanemon"]
Stage3 = ["Gabumon", "Biyomon", "Agumon","Patamon","Elecmon","Penguinmon","Palmon","Betamon"]

#Base Stats
photo = "('.')"
mon = "Botamon" #random.choice(Stage1)
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
        offense = offense +1
        food = food -1
        print("{0}'s offense increased to {1n}".format(name,offense))
        return

    elif user_input == "defense":
        defense = defense +1
        food = food -1
        print("{0}'s defense increaded to {1}".format(name,defense))
        return

    elif user_input == "speed":
        speed = speed +1
        food = food -1
        print("{0}'s speed increaded to {1}".format(name,speed))
        return

    elif user_input == "brains":
        brains = brains +1
        food = food -1
        print("{0}'s brains increaded to {1}".format(name,brains))
        return

    else: 
        print("please select which stat you would like to train")

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
        user_input = input("Enter your pet's new name > ")
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



    #Evolutions
    # need to fix mon evolved to mon - this shows koromon evolved to koromon
    if mon == "Botamon" and offense|defense|speed|brains > 3:
        mon = "Koromon"
        print ("{0} has evolved into a {1}".format(name,mon))

    if mon == "Koromon" and offense > 9:
        mon = "Agumon"
        print ("{0} has evolved into a {1}".format(name,mon))

    if mon == "Koromon" and defense > 9:
        mon = "Gabumon"
        print ("{0} has evolved into a {1}".format(name,mon))