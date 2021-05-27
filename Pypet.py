import random

Stage1 = ["Botamon"]
Stage2 = ["Tsunomon","Koromon"]
Stage3 = ["Gabumon", "Biyomon", "Agumon"]


name = ""
if name == "":
    name = type
photo = "('.')"
type = "Botamon"
age = 0
weight = 2
power = 1
speed = 1
food = 5


def startup_pypet():
    print("Welcome to Pypet!")

def pypet_stats():
    print("This is " + name + " " + photo)
    print(name + " weighs " + str(weight) + " pounds")
    print(name + " has " + str(power) + " power")
    print(name + " has " + str(speed) + " speed")
    print(name + " is a " + type)

    if food < 3:
        print(type + " is hungry!")
    elif food <5:
        print(type + " could eat")
    else:
        print(type + " is full!")

#training
def train():
    global power
    global speed
    global food
    print("Which stat would you like to train?")
    print("Power = " + str(power))
    print("Speed = " + str(speed))    
    user_input = input("> ")

    if user_input == "power":
        power = power +1
        food = food -1
        print(type + "'s power increased to " + str(power))
        return

    elif user_input == "speed":
        speed = speed +1
        food = food -1
        print(type + "'s speed increaded to " + str(speed))
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
        print("'Quit' to close")
        print("'Name' to rename your pet")
        print("'Stats' to see your pet's stats")
        print("'Feed' to feed your pet")
        print("'Train' to improve your pet's stats")

    elif user_input == "name":
        user_input = input("Enter your pet's new name > ")
        user_input = name
            
    elif user_input == "stats":
        pypet_stats()

    elif user_input == "feed":
        weight = weight + 1
        food = food + 1
        if food <3:
            print("You fed " + type + ", but they are still hungry!")

        elif food <5:
            food = food +1
            print ("You fed your " + type)
         
        else:
            print(type +" is stuffed and can't eat anymore!")

    elif user_input == "train":
        train()

    else:
        print("Sorry there was an error. Type 'commands' to see a list of valid commands")



    #Evolutions
    # need to fix type evolved to type - this shows koromon evolved to koromon
    if type == "Botamon" and power > 4 and food > 2:
        type = random.choice(Stage2)
        print ( + " has evolved to " + type)

    if type == "Koromon" and power > 9 and food > 2:
        type = "Agumon"
        print (type + " has evolved into " + type)

    if type == "Tsunomon" and power > 9 and food > 2:
        type = "Gabumon"
        print (type + " has evolved into " + type)

    if  type == "Koromon" or "Tsunamon" and speed > 9 and food > 2:
        type = "Biyomon"
        print (type + " has evolved into " + type)