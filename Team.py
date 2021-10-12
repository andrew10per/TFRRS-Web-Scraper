'''
A Class that defines a team.
A team holds a name string, and holds an array (members) of Athletes in it.

'''
import Athlete
import json
import os

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def printTeam(self):
        for i in self.members:
            i.printAthlete()
            print()
    
    #Dumps team info to JSON in format:
    #{Team NAME : {Athlete NAME: {PRS}}, {Athlete NAME: {PRS}} ....}
    def outputToJSON(self, filename):
        exportdict = {}
        helperdict = {}
        for i in self.members:
           helperdict[i.name] = i.prs
           
        exportdict[self.name] = helperdict
        jsonEXP = json.dumps(exportdict, indent = 1)
        
        with open(filename, "w") as outfile:
            outfile.write(jsonEXP)







    
