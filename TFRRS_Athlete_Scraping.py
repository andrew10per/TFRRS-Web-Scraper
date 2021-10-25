
'''
    A Main running file that contains methods to get and 
    create athletes/teams. Uses BeautifulSoup to parse TFRRS HTML, 
    and can look for specific athletes or whole teams. Teams can be saved to
    .json files and later would like to add functionality to re-import giving ability
    to save and compare Teams. 
'''
import requests
from bs4 import BeautifulSoup
import Athlete
import Team
import os


def getAthlete(url):
    #https://www.tfrrs.org/athletes/4205455.html"
    # Andrew P URL "https://www.tfrrs.org/athletes/7388738"

    #Saves the HTML data into variable page
    page = requests.get(url)


    '''
        #saving HTML Data into file
        html = open("CC_TFRRS.html","w")
        html.write(page.text)
        html.close()
    '''

    #creates a BS object based on the content inside of page
    #Makes an html parser
    soup = BeautifulSoup(page.content, "html.parser")



    #creates an object which restricts our search to just the top table of PRS
    top_table = soup.find("table", class_ = "table bests")

    #Searches for the name of athlete (and class) and returns
    name_html = soup.find("h3", class_ = "panel-title large-title")
    name = name_html.text.strip()
    


    #searches for list of events Athlete has participated in
    events_html = top_table.find_all("td", class_ = "panel-heading-text font-weight-500")


    #Searches for times. Theoretically, the indicies of these times should
    #line up with the list of events so that events[0] is the given
    #distance of times[0]
    times_html = top_table.find_all("td", class_ = "panel-heading-normal-text")

    #es works on garnering just the text from each event to begin the process of
    #Actually setting up a list of events the athlete has competed in.
    events = []

    for e in events_html:
        newstr = e.text.strip()
        newstr = newstr.replace('(XC)', "")
        newstr = newstr.strip()
        events.append(newstr)
        
        
    #timexTxt is the list of times only.
    times = []

    #strips times down to just the string of time.
    for t in times_html:
        times.append(t.text.strip())
        
        
    Person = Athlete.Athlete(name,events,times)
    return Person
    
    
        

def getTeam(url):
    #Saves the HTML data into variable page
    page = requests.get(url)
    team = Team.Team("Canisius", [])

    #creates a BS object based on the content inside of page
    #Makes an html parser
    soup = BeautifulSoup(page.content, "html.parser")

    #Creates a search inside of the table that holds the rosters
    roster_table = soup.find("table", class_ = "tablesaw table-striped table-bordered table-hover")

    #For line in the roster table that is defined by "a", this
    #loop will extract the link for every athleter on the team, and then
    #run the getAthlete() function which returns an athlete object to be appended
    #to the team members list.
    for line in roster_table.find_all("a"):
        link = "http:"
        link = link + line.get('href')
        team.members.append(getAthlete(link))

    #Prints out the team sequentially and returns the team.
    team.printTeam()
    return team
    

#"https://www.tfrrs.org/teams/NY_college_m_Niagara.html"
#sample team URL ^^^


