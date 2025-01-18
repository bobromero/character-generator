#character generator

#i want to get a random name and stats
#the name can be anything, maybe from a library of names somewhere
#the stats are going to be random with each one starting at 20 and ranging from 0-99
import random
from names_generator import generate_name
statline = [20,20,20,20,20,20] # str,dex,health,confidence,int,charisma
stats = ["Strength", "Dexterity", "Health", "Confidence", "Intelligence", "Charisma"]

#i want to use all the available Points
#the system I am coming up with is


# I could traverse through the stats randomly and assign the remaining points to the last stat
# this could create less even characters that are good at 1 thing, as well as whatever the random assignment gives



def genCharacter():
    availablePoints = 20
    for i in range(0,len(statline)):
        x = random.randint(-1,1)
        if x > 0:
            amount = random.randint(1,20) 

            if availablePoints < amount:
                amount = availablePoints
            availablePoints -= amount;
            addPoints(amount,i)
        elif x < 0:
            amount = random.randint(1,20) 

            if statline[i] < amount:
                amount = statline[i] 
            availablePoints += amount
            removePoints(amount,i)
    if availablePoints > 0:
        statline[len(statline)-1] += availablePoints
def addPoints(amount, stat): 
    statline[stat] += amount
def removePoints(amount, stat):
    statline[stat] -= amount

ing = "" 
while ing != "e":
    statline = [20,20,20,20,20,20]
    availablePoints = 20
    genCharacter()
    random.shuffle(statline) 
    for i in range(0,len(stats)):
        print(stats[i], ":\t", statline[i]) 
    print("Name: ", generate_name())

    ing = input()
