'''
A Class that defines an athlete
Athlete holds a name string ( which can also include Class)
Athlete holds an array of events, and an array of times.
These array's should be passed in mathcing
Therefore if events[0] is a 5000, then times[0] should be a 5000 time.

Written by Andrew Perreault
Canisius College Computer Science Student

'''

class Athlete:
    def __init__(self, name, events, times):
        self.name = name
        self.prs = {events[i]: times[i] for i in range(len(events))}

    def printAthlete(self):
        print(self.name)
        #prints out event, and time to go with it.
        print(self.prs)

    
        
