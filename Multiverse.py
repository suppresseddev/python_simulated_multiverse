#Prereqs
from ESLV2 import *
from time import *
from random import random
from random import randint
from _global import *

from universes import *
from planets import *
from nations import *

#Setup Code
#   This will be set up later
globalannouncer = TABIMC("ANNOUNCEMENT")
globalannouncer.role("SIMULATION", "< >")
AllUniverses = []
AllPlanets = []
AllNations = []
#Install Code
#   Grab existing objects and set them up for iteration.
Universe1 = Universe("Universe1")
Planet1 = Planet("Planet", Universe1)
AllUniverses.append(Universe1)
AllPlanets.append(Planet1)
#Live Code
fastforward = False
def runUniverses():
    generic_header("UNIVERSES")
    for universe in AllUniverses:
        universe.event()
        universe.status()
        if not(fastforward):
            sleep(2)
def runPlanets():
    generic_header("PLANETS")
    for planet in AllPlanets:
        if not(fastforward):
            sleep(2)
iterations = 0
while True:
    fastforward = False
    userinput = input("Awaiting input... \n>")
    try:
        userinput = int(userinput)
        fastforward = True
    except:
        print("Doing something else.")
        userinput = 1
    for null in range(0,userinput):
        iterations += 1
        globalannouncer.say("Beginning iteration #"+str(iterations)+"...")
        runUniverses()
        runPlanets()
        globalannouncer.say("Iteration #"+str(iterations)+" Complete!")