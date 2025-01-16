#character generator

#i want to get a random name and stats
#the name can be anything, maybe from a library of names somewhere
#the stats are going to be random with each one starting at 20 and ranging from 0-99
import random

statline = [20,20,20,20,20,20] # str,dex,health,confidence,int,charisma

availablePoints = 20


def genCharacter():
    for i in range(0,len(statline)):
        x = random.randint(-1,1)
        if x > 0:
            addPoints(random.randint(1,20),i)
        elif x < 0:
            removePoints(random.randint(1,20),i)
    print("str,dex,health,confidence,int,charisma")
    print(statline)
def addPoints(amount, stat):
    statline[stat] += amount

def removePoints(amount, stat):
    statline[stat] -= amount


genCharacter()
