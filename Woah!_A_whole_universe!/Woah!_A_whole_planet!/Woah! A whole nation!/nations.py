#Prereqs
from ESLV2 import *
from time import *
from random import random
from random import randint
from _global import *
class Nation:
    def __init__(self):
        #Create some number of attributes for a nation.
        self.Info = []
        self.Info = ["Title", "Population", "Net Worth"]
        #Population Parameters (set later)
        self.DeathRate = 0
        self.BirthRate = 0
        self.ImmigrationRate = 0
        self.EmmigrationRate = 0
        #Economic Parameters (set later)
        self.Imports = 0.00
        self.Exports = 0.00