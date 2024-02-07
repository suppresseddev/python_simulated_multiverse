#This will simulate universal activity and forces.
#Prereqs
from ESLV2 import *
from time import *
from random import random
from random import randint
from _global import *
class Universe:
    def __init__(self, name):
        #The universe name will NOT be changeable!
        self.Name = str(name)
        #Uncontrollable properties that affect planets.
        self.Stability = 0
        self.GoodLuck = 0
        self.BadLuck = 0
        self.Exists = False
        #"Random Chance Value" (0-yet to be determined)
        #Determines random events. Changes by chance.
        self.RCV = randint(0, 9999999999)
        #Making the universe's TABIMC
        self.announcer = TABIMC(self.Name)
        self.announcer.role("UNIVERSE", "[ ]")
    def luck(self):
        #When luck < 1 pass False
        #If luck > 1, pass True
        good = random()*self.GoodLuck
        bad = random()*self.BadLuck
        if debug:
            print("'Good' Value")
            print(good)
            print("'Good' Value")
            print(bad)
            print()
        if(good-bad >= 1):
            return(True)
        if(good-bad < 1):
            return(False)
    def event(self):
        if self.Stability < -1000:
            return()
        #Pick row from the list and grab pertinent information.
        with open(r"C:\Users\wolfs\Documents\Post FLVS Python\Woah!_A_whole_multiverse!\Woah!_A_whole_universe!\RandomUniversalEvents.csv", 'r') as uEvents:
            rawdata = str(uEvents.read()).replace('\n', ',')
            rawdata = rawdata.split(',')
            potential_eventindex = []
            for index in range(0,6):
                rawdata.pop(0)
            if debug:
                print("Raw Data")
                print(rawdata)
                print()
            for item in rawdata:
                if rawdata.index(item) in range(0, len(rawdata), 6):
                    if rawdata[rawdata.index(item)] != "":
                        potential_eventindex.append(rawdata[rawdata.index(item)])
            if debug:
                print("Potential Events")
                print(potential_eventindex)
                print()
            #Perfected the above code!
            chosen_event = randint(0, len(potential_eventindex)-1)
            chosen_event = rawdata.index(potential_eventindex[chosen_event])
            eventName = str(rawdata[chosen_event])
            eventMsg = str(rawdata[chosen_event+1])
            eventGL = int(rawdata[chosen_event+2])
            eventBL = int(rawdata[chosen_event+3])
            eventSB = int(rawdata[chosen_event+4])
            if rawdata[chosen_event+5].upper() == "YES":
                eventAR = True
            else:
                eventAR = False
        if debug:
            print("Selected Event Info")
            print(eventName)
            print(eventMsg)
            print(eventGL)
            print(eventBL)
            print(eventSB)
            print(eventAR)
            print()
        #Time to do the event's stuff!
        if eventName == "The Big Bang":
            if not(self.Exists):
                self.Exists = True
            else:
                return()
        if not(self.Exists):
            self.announcer.say("The deafening silence continues...")
            return()
        self.announcer.say(eventMsg)
        #Background Event Stuff
        self.GoodLuck += eventGL
        if self.GoodLuck > 1000:
            self.GoodLuck = 1000
        self.BadLuck += eventBL
        if self.BadLuck > 1000:
            self.BadLuck = 1000
        self.Stability += (eventSB+(randint(-500,500)))
        if (eventAR):
            self.announcer.say("The balance is shifting!")
            self.Stability += randint(-1000, 1000)
            self.RCV = randint(0, 9999999999)
        if debug:
            print("New Universe Stats")
            print("Good Luck")
            print(self.GoodLuck)
            print("Bad Luck")
            print(self.BadLuck)
            print("Stability")
            print(self.Stability)
            print("Random Chance Value")
            print(self.RCV)
            print()
    def status(self):
        #Give a full length status report of public information.
        indented_header(self.Name, 10)
        if not(self.Exists):
            print("Has not yet formed...")
            return()
        if self.Stability < -1000:
            print("This universe has collapsed...")
            return()
        print("Stability: "+str(self.Stability))



