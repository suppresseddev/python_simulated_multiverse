#Prereqs
from ESLV2 import *
from time import *
from random import random
from random import randint
from _global import *
class Planet:
    def __init__(self, Name, Location):
        #Set the name of the planet
        self.Name = str(Name)
        #Set the parent universe of the planet
        self.Universe = Location
        #Planet Statistics
        self.Value = randint(0, 10000)
        #Contextually, it is in fahrenheit.
        self.Temperature = randint(-300, 300)
        self.WeatherIntensity = randint(0, 1000)
        #Planet Health starts at 5,000 and caps at 10,000.
        self.Health = 5000
        #Durability will reduce the impact of destructive events.
        #It can only decrease.
        self.Durability = randint(-100, 2000)
    def rollGL(self):
        pick = randint(0,1000)
        if debug:
            print("Is the first number less than the latter?")
            print(str(pick)+" vs "+str(self.Universe.GoodLuck))
        return(pick < self.Universe.GoodLuck)