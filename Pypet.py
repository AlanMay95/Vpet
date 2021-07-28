import random
from tkinter import *

root = Tk()

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

#Digilist
Starters = []
Starters.append(Digi("Botamon",0,1,1,1,1,[""]))
Starters.append(Digi("Poyomon",0,1,1,1,1,[""]))
Starters.append(Digi("Punimon",0,1,1,1,1,[""]))
Starters.append(Digi("Yuramon",0,1,1,1,1,[""]))

Digilist = []
Digilist.append(Digi("Koromon",1,3,3,3,3,["Botamon"]))
Digilist.append(Digi("Tokomon",1,3,3,3,3,["Poyomon"]))
Digilist.append(Digi("Tsunomon",1,3,3,3,3,["Punimon"]))
Digilist.append(Digi("Tanemon",1,3,3,3,3,["Yuramon"]))
Digilist.append(Digi("Agumon",2,10,5,5,5,["Koromon"]))
Digilist.append(Digi("Gabumon",2,5,10,10,5,["Koromon"]))
Digilist.append(Digi("Patamon",2,10,5,5,10,["Tokomon"]))
Digilist.append(Digi("Biyomon",2,5,5,10,5,["Tokomon"]))
Kunemon=Digi("Kunemon",2,15,15,15,15,["Koromon","Tokomon","Tsunomon","Tanemon"])
Digilist.append(Kunemon)
Digilist.append(Digi("Electmon",2,10,5,10,5,["Tsunomon"]))
Digilist.append(Digi("Penguinmon",2,5,5,10,10,["Tsunomon"]))
Digilist.append(Digi("Palmon",2,5,5,5,10,["Tanemon"]))
Digilist.append(Digi("Betamon",2,5,10,5,5,["Tanemon"]))

#Starter
self = random.choice(Starters)
name = self.mon

#Evo

def Evo(): 
    for obj in Digilist: 
        if self.mon in obj.evo and self.offense >= obj.offense and self.defense >= obj.defense and self.speed >= obj.speed and self.brains >= obj.brains:
            self.age = obj.age
            self.mon = obj.mon
            line2.config(text ="Type: {}".format(self.mon))
            line7.config(text ="Age: {}".format(self.age))
            line8.config(text ="{0} has digivoled into {1}".format(name,self.mon))
            
def KunemonEvo():
        if self.mon in Kunemon.evo and (self.offense > Kunemon.offense or self.defense > Kunemon.defense or self.speed > Kunemon.speed or self.brains > Kunemon.brains):
            self.age = Kunemon.age
            self.mon = Kunemon.mon
            line2.config(text ="Type: {}".format(self.mon))
            line7.config(text ="Age: {}".format(self.age))
            line8.config(text ="{0} has digivoled into {1}".format(name,self.mon))

def Evos():
    Evo()
    KunemonEvo()

#Rename
def Re():
    Rename =Tk()

    R2 = Label(Rename, text = "Type your name for {}".format(name))
    R3 = Entry(Rename)

    def xyz():
        global name
        name = R3.get()
        line1.config(text="Name: {}".format(name))
        Rename.destroy()

    R4 = Button(Rename, text = "Confirm", command = xyz)

    R2.grid(row=0,column=0)
    R3.grid(row=1,column=0)
    R4.grid(row=2,column=0)

#training
def Train():
    Training =Tk()

    #Stat Gain
    def TrainO():
        RGO = random.randint(1,5)
        self.offense = self.offense + RGO
        T2.config(text= "Offense: {}".format(self.offense))
        T6.config(text= "Offense has increase by {}".format(RGO))
    def TrainD():
        RG = random.randint(1,5)
        self.defense = self.defense + RG
        T3.config(text= "Defense: {}".format(self.defense))
        T6.config(text= "Defense has increase by {}".format(RG))
    def TrainS():
        RG = random.randint(1,5)
        self.speed = self.speed + RG
        T4.config(text= "Speed: {}".format(self.speed))
        T6.config(text= "Speed has increase by {}".format(RG))
    def TrainB():
        RG = random.randint(1,5)
        self.brains = self.brains + RG
        T5.config(text= "Brains: {}".format(self.brains))
        T6.config(text= "Brains has increase by {}".format(RG))

    #Exit  
    def EndT():
        line3.config(text ="Offense: {0}".format(self.offense))
        line4.config(text ="Defense: {}".format(self.defense))
        line5.config(text ="Speed: {}".format(self.speed))
        line6.config(text ="Brains: {}".format(self.brains))
        Evos()
        Training.destroy()
        

    T1 = Label(Training, text = "Select that stat you wish to train")
    T2 = Button(Training, text = "Offense: {}".format(self.offense), command = TrainO)
    T3 = Button(Training, text = "Defense: {}".format(self.defense), command = TrainD)
    T4 = Button(Training, text = "Speed: {}".format(self.speed), command = TrainS)
    T5 = Button(Training, text = "Brains: {}".format(self.brains), command = TrainB)
    T6 = Label(Training, text="")
    T7 = Button(Training, text = "Finish training", command = EndT)

    T1.grid(row=0,column=0,columnspan=2)
    T2.grid(row=1,column=0)
    T3.grid(row=1,column=1)
    T4.grid(row=2,column=0)
    T5.grid(row=2,column=1)
    T6.grid(row=3,column=0,columnspan=2)
    T7.grid(row=4,column=0,columnspan=2)

#root window
line1 = Label(root, text="Name: {0}".format(name))
line2 = Label(root, text="Type: {0}".format(self.mon))
line3 = Label(root, text="Offense: {0}".format(self.offense))
line4 = Label(root, text="Defense: {}".format(self.defense))
line5 = Label(root, text="Speed: {}".format(self.speed))
line6 = Label(root, text="Brains: {}".format(self.brains))
line7 = Label(root, text="Age: {}".format(self.age))
line8 = Label(root, text="")

line1.grid(row=0, column=0)
line2.grid(row=0, column=1)
line3.grid(row=1, column=0)
line4.grid(row=1, column=1)
line5.grid(row=2, column=0)
line6.grid(row=2, column=1)
line7.grid(row=3, column=0)
line8.grid(row=4, column=0, columnspan = 2)

button1 = Button(root, text="Rename", command = Re)
button2 = Button(root, text="Training", command = Train)

button1.grid(row=5, column =0)
button2.grid(row=5, column =1)

root.mainloop()