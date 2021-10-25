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
        
        try:
            with open(filename, "w") as outfile:
                outfile.write(jsonEXP)
        except:
            print("Invalid file name.")

    #Accepts a JSON as input and then imports the .json file.
    def inputFromJSON(self, filename):
        importdict = {}
        try:
            f = open(filename, 'r')
        except:
            print("Invalid file name.")
        importdict = json.load(f)
        for key in importdict:
            self.name = key
            for key2 in importdict[key]:
                newAthlete = Athlete.Athlete(key2,[],[])
                for key3 in importdict[key][key2]:
                    newAthlete.prs[key3] = importdict[key][key2][key3]
                self.members.append(newAthlete)




team = Team("Hello",[])
team.inputFromJSON("Niagara.json")
team.printTeam()







    
